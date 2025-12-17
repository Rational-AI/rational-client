# Rational Client

[![PyPI version](https://badge.fury.io/py/rational-client.svg)](https://badge.fury.io/py/rational-client) <!-- Placeholder: This badge will work once the package is published to PyPI -->


`rational-client` is the official Python client for interacting with the [Rational AI platform](https://rational.is/). It provides a high-level, object-oriented interface to manage knowledge bases, resources, annotations, and perform powerful semantic searches.

This client is designed to make it easy to integrate your Python applications with Rational AI, enabling you to build powerful workflows for data processing, analysis, and retrieval.

## Key Features

- **Knowledge Base Management**: Programmatically interact with your Rational AI knowledge bases.
- **Resource and Annotation Handling**: Create, retrieve, update, and delete resources and their associated annotations (text chunks, images, comments, etc.).
- **Semantic Search**: Find similar annotations or resources using vector embeddings.
- **Keyword Extraction**: Automatically extract relevant keywords from your text data using either rule-based methods or advanced LLM-based extraction.
- **Data Synchronization**: Upload and manage files (`SyncedResource`) within your knowledge base, which can then be processed by automated workflows.
- **Object-Oriented Interface**: A clean, intuitive API that maps directly to Rational AI concepts like `Knowledge`, `RationalResource`, and `Annotation`.

## Installation

You can install `rational-client` directly from its public GitHub repository using `pip`.

```bash
pip install git+https://github.com/Rational-AI/rational-client.git
```

The package requires **Python 3.12 or higher**.

## Configuration

The client requires two environment variables to be set for authentication and for connecting to the correct backend instance.

- `BACKEND_ADDRESS`: The URL of your Rational AI backend.
- `BACKEND_API_KEY`: Your unique API key for authentication.

You can set these variables in your shell before running your application:
```bash
export BACKEND_ADDRESS="https://your-backend.rationalai.com"
export BACKEND_API_KEY="your_secret_api_key_here"
```

## Quick Start

Here’s a simple example to get you started. This snippet demonstrates how to connect to a knowledge base, create a resource, add a text annotation, and perform a similarity search.

```python
import os
from uuid import UUID

# It's recommended to set environment variables before importing the client
# to ensure all modules are initialized with the correct credentials.
# os.environ["BACKEND_ADDRESS"] = "http://your-backend-url"
# os.environ["BACKEND_API_KEY"] = "your-api-key"

from rational_client.core import Knowledge, AnnotationType

# --- 1. Connect to your Knowledge Base ---
# Replace with the actual UUID of your Knowledge Base
try:
    KNOWLEDGE_ID = UUID("your-knowledge-id-here")
    knowledge = Knowledge(knowledge_id=KNOWLEDGE_ID)
    print(f"Successfully connected to Knowledge Base: '{knowledge.name}'")
except Exception as e:
    print(f"Error connecting to Knowledge Base. Ensure your KNOWLEDGE_ID and environment variables are correct. Details: {e}")
    exit()

# --- 2. Create a new Resource (Relevant) ---
print("\nCreating a relevant resource...")
resource_1 = knowledge.create_resource(
    name="Machine Learning Document",
    category="Technology",
    tags=["ml", "ai"]
)
print(f"Resource '{resource_1.name}' created with ID: {resource_1.resource_id}")

# --- 3. Add an Annotation to the relevant resource ---
print("Adding a relevant text annotation...")
text_content_1 = "Machine learning enables computers to learn from data without being explicitly programmed."
annotation_1 = resource_1.add_annotation(
    annotation_type=AnnotationType.CHUNK,
    data={"content": text_content_1},
    embedding=knowledge.embed_one(text_content_1)
)
print(f"Annotation created with content: '{annotation_1.data['content']}'")


# --- 4. Create an UNRELATED Resource ---
print("\nCreating an unrelated resource to test search relevance...")
resource_2 = knowledge.create_resource(
    name="History of Rome",
    category="History",
    tags=["rome", "ancient"]
)
print(f"Resource '{resource_2.name}' created with ID: {resource_2.resource_id}")

# --- 5. Add an Annotation to the UNRELATED resource ---
print("Adding an unrelated text annotation...")
text_content_2 = "The Roman Empire was one of the most powerful economic, cultural, and military forces in the world."
annotation_2 = resource_2.add_annotation(
    annotation_type=AnnotationType.CHUNK,
    data={"content": text_content_2},
    embedding=knowledge.embed_one(text_content_2)
)
print(f"Annotation created with content: '{annotation_2.data['content']}'")


# --- 6. Perform a Similarity Search ---
print("\nPerforming a similarity search for a query about machine learning...")
# First, we need a vector to search with. Let's embed a query.
query_text = "What is machine learning?"
query_vector = knowledge.embed_one(query_text)

# Now, find the single most similar annotation.
# This should return the annotation from `resource_1` and ignore `resource_2`.
similar_annotations = knowledge.find_similar(query_vector=query_vector, top_k=1)

if similar_annotations:
    top_result = similar_annotations[0]
    print(f"Found a similar annotation with a score of {top_result.score:.4f}:")
    print(f"  - Content: '{top_result.annotation.data['content']}'")
    print(f"  - In Resource: '{top_result.rational_resource.name}' (ID: {top_result.rational_resource.id})")
else:
    print("No similar annotations found.")
```

## Core Concepts

The client is built around a few core classes that map to the main entities in Rational AI:

- **`Knowledge`**: The main entry point. It represents a knowledge base and is used to manage resources, perform searches, and handle embeddings.
- **`RationalResource`**: Represents a conceptual entity within your knowledge base (e.g., a document, a product, a user). It acts as a container for annotations.
- **`Annotation`**: A piece of information attached to a `RationalResource`. This can be a text chunk (`CHUNK`), an image, a comment, or any other data type. Annotations are the primary target for semantic search.
- **`SyncedResource`**: Represents a raw file (e.g., PDF, TXT, JSON) uploaded to the platform. These files can be processed by automated workflows to create `RationalResource`s and `Annotation`s.

## Advanced Examples

For more complex use cases and detailed workflow implementations, please refer to the examples in the `examples/` directory of the repository. These demonstrate how to process different file types, create structured data, and build relationships between resources.

## License

This project is licensed under the **Apache 2.0 License**. See the `LICENSE` file for more details.