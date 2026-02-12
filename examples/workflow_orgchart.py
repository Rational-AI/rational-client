#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "rational-client",
# ]
# ///
import json
import sqlite3
import tempfile

from rational_client.core import File, Knowledge, SyncedResource
from rational_client.utils import run


def process(document: SyncedResource, options: dict):
    # Parse the JSON data from the resource
    content = document.get_data()
    data = json.loads(content)

    # Create a temp SQLite database file
    with tempfile.NamedTemporaryFile(suffix=".db") as db_file:
        db_path = db_file.name

        # Create the schema
        with sqlite3.connect(db_path) as conn:
            cur = conn.cursor()

            # Create database schema
            cur.execute("""
                CREATE TABLE IF NOT EXISTS company_summary (
                    company_name TEXT COLLATE NOCASE PRIMARY KEY,
                    hq_city TEXT COLLATE NOCASE,
                    hq_country TEXT COLLATE NOCASE,
                    annual_revenue REAL,
                    shipping TEXT COLLATE NOCASE
                );
            """)

            cur.execute("""
                CREATE TABLE IF NOT EXISTS company_channels (
                    company_name TEXT COLLATE NOCASE,
                    channel TEXT COLLATE NOCASE
                );
            """)

            cur.execute("""
                CREATE TABLE IF NOT EXISTS employees (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT COLLATE NOCASE,
                    title TEXT COLLATE NOCASE,
                    department TEXT COLLATE NOCASE,
                    location TEXT COLLATE NOCASE,
                    email TEXT COLLATE NOCASE,
                    employeeId TEXT COLLATE NOCASE,
                    startDate TEXT COLLATE NOCASE,
                    salary_eur REAL,
                    dotted_line_to TEXT COLLATE NOCASE,
                    manager_id INTEGER,
                    root BOOLEAN,
                    resource_id TEXT
                );
            """)

            knowledge = Knowledge(document.knowledge_id)

            # Insert company summary
            summary = data["summary"]
            company_name = summary.get("company_name", "Unknown Company")
            cur.execute(
                "INSERT OR REPLACE INTO company_summary (company_name, hq_city, hq_country, annual_revenue, shipping) "
                "VALUES (?, ?, ?, ?, ?)",
                (
                    company_name,
                    summary.get("hq_city"),
                    summary.get("hq_country"),
                    summary.get("annual_revenue"),
                    summary.get("shipping"),
                ),
            )

            # Insert channels
            for channel in summary.get("channels", []):
                cur.execute(
                    "INSERT INTO company_channels (company_name, channel) VALUES (?, ?)",
                    (summary.get("company_name"), channel),
                )

            # Dictionary to store employee resources by employeeId for dotted_line relation
            employee_resources = {}
            # list of dotted lines to create at the end of the process
            dotted_lines = []

            # Recursive function to insert employees and their reports
            def insert_employee(node, manager_id=None, manager_resource=None, root=False):
                # Create a rational resource for the employee
                employee_resource = knowledge.create_resource(
                    name=node.get("name"),
                    category=node.get("department", "Unknown Department"),
                    notes=f"{node.get('title', '')} in {node.get('department', '')}, email: {node.get('email', '')}",
                    tags=[],
                    synced_resource_id=document.id,
                )
                employee_resource_id = employee_resource.resource_id

                cur.execute(
                    """
                    INSERT INTO employees (
                        name, title, department, location, email, employeeId, startDate, salary_eur,
                        dotted_line_to, manager_id, root, resource_id
                    )
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                    """,
                    (
                        node.get("name"),
                        node.get("title"),
                        node.get("department"),
                        node.get("location"),
                        node.get("email"),
                        node.get("employeeId"),
                        node.get("startDate"),
                        node.get("salary_eur"),
                        json.dumps(node.get("dotted_line_to", [])),
                        manager_id,
                        int(root),
                        str(employee_resource_id),
                    ),
                )
                emp_id = cur.lastrowid

                # Store employee resources by employeeId for dotted_line relation
                emp_key = node.get("employeeId")
                if emp_key:
                    employee_resources[emp_key] = employee_resource

                # Recursively insert reports first, so dotted_line_to can reference them
                for report in node.get("reports", []):
                    report_resource = insert_employee(
                        report,
                        manager_id=emp_id,
                        manager_resource=employee_resource,
                        root=False,
                    )
                    report_resource.add_relation(employee_resource, "reports")

                # Add "dotted_line" relation if dotted_line_to is present and already inserted
                for dotted_id in node.get("dotted_line_to", []):
                    dotted_lines.append((employee_resource, dotted_id))

                return employee_resource

            insert_employee(data["org_chart"], manager_id=None, manager_resource=None, root=True)
            for employee_resource, dotted_id in dotted_lines:
                dotted_line_resource = employee_resources.get(dotted_id)
                if dotted_line_resource:
                    employee_resource.add_relation(dotted_line_resource, "dotted_line")

            conn.commit()

        # Create a RationalResource for the SQLite database
        with open(db_path, "rb") as f:
            _ = knowledge.upload_synced_resource(
                name="orgchart.db",
                contents=File(f, file_name="orgchart.db", mime_type="application/x-sqlite3"),
                parent_id=document.id,
            )


run(process)
