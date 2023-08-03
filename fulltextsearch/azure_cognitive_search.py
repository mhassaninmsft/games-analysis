
from fulltextsearch.full_text_search import FullTextSearchInterface, FullTextSearchResult
import os
from azure.core.credentials import AzureKeyCredential
from azure.search.documents import SearchClient

index_name = "nycjobs"
# Get the service endpoint and API key from the environment
endpoint = os.environ["SEARCH_ENDPOINT"]
key = os.environ["SEARCH_API_KEY"]


class AzureCognitiveSearch(FullTextSearchInterface):
    def __init__(self, config):
        self.config = config
        # Create a client
        self.credential = AzureKeyCredential(key)
        self.client = SearchClient(endpoint=endpoint,
                                   index_name=index_name,
                                   credential=self.credential)

    def search(self, request: str) -> list[FullTextSearchResult]:
        """Search for the request."""
        pass

    def add_document(self, document: str, id: str):
        """Add a document to the search."""
        pass
