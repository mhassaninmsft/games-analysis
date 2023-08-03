import os
from azure.core.credentials import AzureKeyCredential
from azure.search.documents import SearchClient
from fulltextsearch.create_index import GameSearchObject

from models import get_games

index_name = "games"
endpoint = os.environ["SEARCH_ENDPOINT"]
key = os.environ["SEARCH_API_KEY"]


def search_for_documents(search_term: str):
    # DOCUMENT = {
    #     'Category': 'Hotel',
    #     'hotelId': '1000',
    #     'rating': 4.0,
    #     'rooms': [],
    #     'hotelName': 'Azure Inn',
    # }

    search_client = SearchClient(endpoint, index_name, AzureKeyCredential(key))
    results = search_client.search(search_text=search_term, top=10)
    print(results)
    for result in results:
        print(
            f"{result['@search.score']} {result['gameName']} {result['gameUrl']}")
        # print(f"Game name: {result['gameName']}")
