
from Actions.actions import ActionsEnum, ChatBotAction
from faq_embeddings import FaQEmbedding


class SearchFaqAction(ChatBotAction):
    def __init__(self, search_faq_service: FaQEmbedding):
        self.search_faq_service = search_faq_service

    def get_closest_docs(self, request: str):
        """ Search the FAQ for the request."""
        docs = self.search_faq_service.search_faq(request)
        return docs

    def execute(self) -> ActionsEnum:
        """ Execute the action."""
        pass
