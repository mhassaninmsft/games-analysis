
from chroma import ChromaEmbedding
from csvReader import get_data
import uuid


class FaQEmbedding:
    def __init__(self) -> None:
        collection_name = "faq_collection"
        self.chroma_embedding = ChromaEmbedding(
            collection_name=collection_name)

    def create_faq_embeddings(self) -> None:
        """ Create FAQ Embeddings from the FAQ data."""
        data = get_data()
        for item in data:
            val = str(item)
            print(val)
            my_id = uuid.uuid4()
            self.chroma_embedding.create_embedding(val, id=str(my_id))

    def search_faq(self, request: str):
        """ Search the FAQ for the request."""
        embedding = self.chroma_embedding.create_embedding_only(request)
        return self.get_closest_match(embedding)

    def get_closest_match(self, embedding):
        """ Get the closest match to the embedding."""
        return self.chroma_embedding.search_by_embedding(embedding=embedding)
