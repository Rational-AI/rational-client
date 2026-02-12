import random
import unittest

if True:
    # we run this before other imports because of its side-effects
    from .utils import create_knowledge, delete_knowledge

from rational_client.core import AnnotationType, BboxSelector, RationalResource
from rational_client.deps.backend_knowledge_v0_client.models import (
    RationalResourceDto,
    SearchResultDto,
    SyncedResourceDtoPage,
)
from rational_client.deps.backend_knowledge_v0_client.types import File

random.seed(42)  # For reproducibility


class TestKnowledgeResourceIntegration(unittest.TestCase):
    def setUp(self):
        # Disable keyword extraction for tests to avoid unnecessary LLM calls
        self.knowledge = create_knowledge(name="Test Knowledge", allow_keywords_extraction=False)
        self.resource_name = "Test Resource"
        self.resource = self.knowledge.create_resource(
            name=self.resource_name,
            notes="Test notes",
            tags=["tag1", "tag2"],
        )
        self.resource_id = self.resource.resource_id

        self.annotations = [
            self.resource.add_annotation(
                annotation_type=AnnotationType.CHUNK,
                position=1,
                content="Lorem ipsum",
                data={"content": "Lorem ipsum"},
                embedding=[0.1] * 256,
            ),
            self.resource.add_annotation(
                annotation_type=AnnotationType.CHUNK,
                position=2,
                content="Dolor sit amet",
                data={"content": "Dolor sit amet"},
                embedding=[0.2] * 256,
            ),
            self.resource.add_annotation(
                annotation_type=AnnotationType.IMAGE,
                selector=BboxSelector(kind="bbox", xmax=10, xmin=20, ymax=100, ymin=200),
                data={"page": 3},
            ),
        ]

    def tearDown(self):
        for resource in self.knowledge.get_resources():
            self.knowledge.delete_resource(resource.resource_id)
        delete_knowledge(self.knowledge.knowledge_id)

    def test_get_resource(self):
        resource = self.knowledge.get_resource(self.resource_id)
        self.assertIsInstance(resource, RationalResource)
        self.assertEqual(resource.resource_id, self.resource_id)
        self.assertEqual(resource.knowledge_id, self.knowledge.knowledge_id)
        self.assertEqual(resource.name, self.resource_name)

    def test_get_resource_by_name(self):
        resource = self.knowledge.get_resource_by_name(self.resource_name)
        self.assertIsInstance(resource, RationalResource)
        self.assertEqual(resource.name, self.resource_name)
        self.assertEqual(resource.resource_id, self.resource_id)

    def test_get_resources(self):
        resources = list(self.knowledge.get_resources())
        resource_ids = [r.resource_id for r in resources]
        self.assertIn(self.resource_id, resource_ids)

    def test_update_resource(self):
        new_name = "Updated Resource Name"
        self.resource.name = new_name
        self.resource.save()
        updated = self.knowledge.get_resource(self.resource_id)
        self.assertEqual(updated.name, new_name)

    def test_delete_resource(self):
        result = self.knowledge.delete_resource(self.resource_id)
        self.assertIsNone(result)
        resources = list(self.knowledge.get_resources())
        resource_ids = [r.resource_id for r in resources]
        self.assertNotIn(self.resource_id, resource_ids)


def cosine_similarity(vec1: list[float], vec2: list[float]) -> float:
    """
    Compute the cosine similarity between two vectors.
    Returns a float between -1 and 1.
    """
    from math import sqrt

    if len(vec1) != len(vec2):
        raise ValueError("Vectors must be the same length")

    dot_product = sum(a * b for a, b in zip(vec1, vec2))
    norm1 = sqrt(sum(a * a for a in vec1))
    norm2 = sqrt(sum(b * b for b in vec2))

    if norm1 == 0 or norm2 == 0:
        return 0.0

    return dot_product / (norm1 * norm2)


class TestKnowledgeSimilaritySearchIntegration(unittest.TestCase):
    def setUp(self):
        # Disable keyword extraction for tests to avoid unnecessary LLM calls
        self.knowledge = create_knowledge(name="Test Knowledge for Similarity Search", allow_keywords_extraction=False)
        self.query_vector = [random.uniform(-1, 1) for _ in range(256)]
        for i in range(3):
            resource = self.knowledge.create_resource(name=f"Resource {i}")
            position = 0
            for j in range(3):  # Add multiple annotations per resource
                position += 1
                # Add one annotation with an embedding that matches the query vector
                resource.add_annotation(
                    annotation_type=AnnotationType.CHUNK,
                    position=position,
                    content=f"Matching Annotation {j + 1} for Resource {i + 1}",
                    data={
                        "content": f"Matching Annotation {j + 1} for Resource {i + 1}",
                    },
                    embedding=self.query_vector,
                )
                position += 1
                # Add another annotation with a random embedding
                random_embedding = [random.uniform(-1, 1) for _ in range(256)]
                resource.add_annotation(
                    annotation_type=AnnotationType.CHUNK,
                    position=position,
                    content=f"Random Annotation {j + 1} for Resource {i + 1}",
                    data={
                        "content": f"Random Annotation {j + 1} for Resource {i + 1}",
                    },
                    embedding=random_embedding,
                )
            self.top_k = 3  # Number of top results to return

    def tearDown(self):
        for resource in self.knowledge.get_resources():
            self.knowledge.delete_resource(resource.resource_id)
        delete_knowledge(self.knowledge.knowledge_id)

    def test_find_similar(self):
        results = self.knowledge.find_similar(query_vector=self.query_vector, top_k=self.top_k)
        self.assertIsInstance(results, list)
        self.assertTrue(all(isinstance(r, SearchResultDto) for r in results))
        # Check that the returned annotation embedding matches the query vector
        for r in results:
            self.assertIsInstance(r.rational_resource, RationalResourceDto)
            self.assertIsNotNone(r.annotation.embedding)
            embedding = r.annotation.embedding
            if isinstance(embedding, list) and all(isinstance(x, float) for x in embedding):
                self.assertAlmostEqual(
                    cosine_similarity(self.query_vector, embedding),
                    1.0,
                    places=6,
                    msg="Returned annotation embedding does not match the query vector",
                )
            else:
                self.fail("Annotation embedding is not a valid list of floats")

    def test_find_similar_resources(self):
        results = self.knowledge.find_similar_resources(query_vector=self.query_vector, top_k=self.top_k)
        self.assertIsInstance(results, list)
        self.assertTrue(all(isinstance(r, SearchResultDto) for r in results))
        resource_ids = {r.rational_resource.id for r in results}
        self.assertEqual(len(resource_ids), len(results), "All results should come from different resources")
        # Check that the returned annotation embedding matches the query vector
        for resource_search_result in results:
            embedding = resource_search_result.annotation.embedding
            if isinstance(embedding, list):
                self.assertTrue(all(isinstance(x, float) for x in embedding))
                self.assertAlmostEqual(
                    cosine_similarity(self.query_vector, embedding),
                    1.0,
                    places=6,
                    msg="Returned annotation embedding does not match the query vector",
                )
            else:
                self.fail(f"Annotation embedding is not a valid list of floats, got type: {type(embedding)}")


class TestResourceAnnotationIntegration(unittest.TestCase):
    def setUp(self):
        # Disable keyword extraction for tests to avoid unnecessary LLM calls
        self.knowledge = create_knowledge(name="Test Knowledge for Annotation", allow_keywords_extraction=False)
        self.resource = self.knowledge.create_resource(name="Resource for Annotation Test")
        self.resource_id = self.resource.resource_id
        self.annotation_content = "Test Annotation"
        self.annotation_type = AnnotationType.COMMENT
        self.annotation = self.resource.add_annotation(
            annotation_type=self.annotation_type,
            data={
                "content": self.annotation_content,
            },
        )
        self.annotation_id = self.annotation.annotation_id

    def tearDown(self):
        for resource in self.knowledge.get_resources():
            self.knowledge.delete_resource(resource.resource_id)
        delete_knowledge(self.knowledge.knowledge_id)

    def test_get_annotation(self):
        annotations = list(self.resource.get_annotations())
        annotation_ids = [a.annotation_id for a in annotations]
        self.assertIn(self.annotation_id, annotation_ids)
        found = [a for a in annotations if a.annotation_id == self.annotation_id][0]
        self.assertEqual(found.data["content"], self.annotation_content)
        self.assertEqual(found.annotation_type, self.annotation_type)

    def test_update_annotation(self):
        new_content = "Updated Annotation Content"
        self.annotation.data["content"] = new_content
        self.annotation.save()
        updated = [a for a in self.resource.get_annotations() if a.annotation_id == self.annotation_id][0]
        self.assertEqual(updated.data["content"], new_content)

    def test_delete_annotation(self):
        result = self.resource.delete_annotation(self.annotation_id)
        self.assertIsNone(result)
        annotations = list(self.resource.get_annotations())
        annotation_ids = [a.annotation_id for a in annotations]
        self.assertNotIn(self.annotation_id, annotation_ids)

    def test_clear_annotations(self):
        # Add a second annotation to ensure multiple are deleted
        self.resource.add_annotation(
            annotation_type=AnnotationType.COMMENT,
            content="Another annotation",
            data={
                "content": "Another annotation",
            },
        )
        self.resource.clear_annotations()
        annotations = list(self.resource.get_annotations())
        self.assertEqual(len(annotations), 0)


class TestResourceRelationsIntegration(unittest.TestCase):
    def setUp(self):
        # Disable keyword extraction for tests to avoid unnecessary LLM calls
        self.knowledge = create_knowledge(name="Test Knowledge for Relations", allow_keywords_extraction=False)
        self.resource1 = self.knowledge.create_resource(name="Resource 1")
        self.resource2 = self.knowledge.create_resource(name="Resource 2")
        self.resource1_id = self.resource1.resource_id
        self.resource2_id = self.resource2.resource_id

    def tearDown(self):
        for resource in self.knowledge.get_resources():
            self.knowledge.delete_resource(resource.resource_id)
        delete_knowledge(self.knowledge.knowledge_id)

    def test_add_and_get_relation(self):
        relation_type = "related_to"
        self.resource1.add_relation(
            related_resource=self.resource2,
            type=relation_type,
        )
        relations = list(self.resource1.get_relations())
        self.assertEqual(len(relations), 1)
        relation = relations[0]
        self.assertEqual(relation.type, relation_type)
        relation_ids = [r.related_resource_id for r in relations]
        self.assertIn(self.resource2_id, relation_ids)

    def test_remove_relation(self):
        relation_type = "related_to"
        relation = self.resource1.add_relation(
            related_resource=self.resource2,
            type=relation_type,
        )
        self.resource1.delete_relation(relation.relation_id)
        relations = list(self.resource1.get_relations())
        self.assertEqual(len(relations), 0)

    def test_update_relation(self):
        relation_type = "related_to"
        relation = self.resource1.add_relation(
            related_resource=self.resource2,
            type=relation_type,
        )
        new_type = "new_related_to"
        relation.type = new_type
        relation.save()
        updated_relations = list(self.resource1.get_relations())
        updated_relation = updated_relations[0]
        self.assertEqual(updated_relation.type, new_type)


class TestKnowledgeEmbedIntegration(unittest.TestCase):
    def setUp(self):
        # Disable keyword extraction for tests to avoid unnecessary LLM calls
        self.knowledge = create_knowledge(name="Test Knowledge for Embedding", allow_keywords_extraction=False)

    def tearDown(self):
        delete_knowledge(self.knowledge.knowledge_id)

    def test_embed_text(self):
        text = "This is a test sentence for embedding."
        embedding = self.knowledge.embed_one(text)
        self.assertIsInstance(embedding, list)
        self.assertTrue(all(isinstance(val, float) for val in embedding))
        self.assertGreater(len(embedding), 0, "Embedding should not be empty")

    def test_embed_batch(self):
        texts = [
            "This is the first test sentence.",
            "This is the second test sentence.",
            "This is the third test sentence.",
        ]
        embeddings = self.knowledge.embed_batch(texts)
        self.assertIsInstance(embeddings, list)
        self.assertEqual(len(embeddings), len(texts))
        for embedding in embeddings:
            self.assertIsInstance(embedding, list)
            self.assertTrue(all(isinstance(x, float) for x in embedding))
            self.assertGreater(len(embedding), 0, "Embedding should not be empty")

    def test_get_token_count(self):
        text = "This is a test sentence for getting token count."
        token_count = self.knowledge.get_token_count(text)
        self.assertIsInstance(token_count, int)
        self.assertEqual(token_count, 11)


class TestSyncedResourceIntegration(unittest.TestCase):
    def setUp(self):
        # Disable keyword extraction for tests to avoid unnecessary LLM calls
        self.knowledge = create_knowledge(name="Test Knowledge for Synced Resource", allow_keywords_extraction=False)
        # Create a synced resource for testing
        self.synced_resource_name = "TestSyncedResource"
        # Create a dummy text file
        import io

        contents = b"This is a dummy synced resource file for testing."
        self.synced_resource = self.knowledge.upload_synced_resource(
            name=self.synced_resource_name,
            contents=File(io.BytesIO(contents), file_name=self.synced_resource_name, mime_type="text/plain"),
        )

    def tearDown(self):
        delete_knowledge(self.knowledge.knowledge_id)

    def test_list_synced_resources(self):
        resources = list(self.knowledge.get_synced_resources())
        self.assertIsInstance(resources, list)
        # Check that each resource has expected attributes
        for resource in resources:
            self.assertTrue(hasattr(resource, "id"))
            self.assertTrue(hasattr(resource, "knowledge_id"))

    def test_get_synced_resource_by_name(self):
        # This assumes a synced resource with self.synced_resource_name exists
        resource = self.knowledge.get_synced_resources_paginated(name=self.synced_resource_name)
        self.assertIsNotNone(resource)
        self.assertIsInstance(resource, SyncedResourceDtoPage)
        self.assertEqual(len(resource.items), 1)
        self.assertTrue(resource.items[0].name == self.synced_resource_name)

    def test_delete_synced_resource(self):
        # Delete the synced resource and ensure it is removed
        result = self.knowledge.delete_synced_resource(self.synced_resource.id)
        self.assertIsNone(result)
        resources = list(self.knowledge.get_synced_resources())
        resource_ids = [r.id for r in resources]
        self.assertNotIn(self.synced_resource.id, resource_ids)

    def test_update_synced_resource_name(self):
        # Upload a synced resource to update
        import io

        contents = b"Initial content for update test."
        synced_resource = self.knowledge.upload_synced_resource(
            name="OriginalName",
            contents=File(io.BytesIO(contents), file_name="OriginalName", mime_type="text/plain"),
        )
        # Update the name
        updated_name = "UpdatedName"
        updated_resource = self.knowledge.update_synced_resource(
            id=synced_resource.id,
            name=updated_name,
        )
        self.assertIsNotNone(updated_resource)
        self.assertEqual(updated_resource.id, synced_resource.id)
        self.assertEqual(updated_resource.name, updated_name)

    def test_update_synced_resource_status(self):
        import io

        contents = b"Content for status update test."
        synced_resource = self.knowledge.upload_synced_resource(
            name="StatusTest",
            contents=File(io.BytesIO(contents), file_name="StatusTest", mime_type="text/plain"),
        )
        from rational_client.deps.backend_knowledge_v0_client.models import SyncedResourceStatus

        updated_resource = self.knowledge.update_synced_resource(
            id=synced_resource.id,
            status=SyncedResourceStatus.PROCESSED,
        )
        self.assertIsNotNone(updated_resource)
        self.assertEqual(updated_resource.id, synced_resource.id)
        self.assertEqual(updated_resource.status, SyncedResourceStatus.PROCESSED)

    def test_update_synced_resource_invalid_id_raises(self):
        from uuid import uuid4

        invalid_id = uuid4()
        with self.assertRaises(TypeError):
            self.knowledge.update_synced_resource(id=invalid_id, name="ShouldFail")


if __name__ == "__main__":
    unittest.main()
