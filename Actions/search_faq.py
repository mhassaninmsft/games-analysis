
from faq_embeddings import FaQEmbedding


class SearchFaqAction:
    def __init__(self, search_faq_service: FaQEmbedding):
        self.search_faq_service = search_faq_service

    def get_closest_docs(self, request: str):
        """ Search the FAQ for the request."""
        docs = self.search_faq_service.search_faq(request)
        return docs
    