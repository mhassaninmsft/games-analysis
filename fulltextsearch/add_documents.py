import os
from azure.core.credentials import AzureKeyCredential
from azure.search.documents import SearchClient
from fulltextsearch.create_index import GameSearchObject

from models import get_games

index_name = "games"
endpoint = os.environ["SEARCH_ENDPOINT"]
key = os.environ["SEARCH_API_KEY"]


def add_documents():
    # DOCUMENT = {
    #     'Category': 'Hotel',
    #     'hotelId': '1000',
    #     'rating': 4.0,
    #     'rooms': [],
    #     'hotelName': 'Azure Inn',
    # }

    search_client = SearchClient(endpoint, index_name, AzureKeyCredential(key))

    games = get_games()
    # break games into 10000 chunks
    games1 = games[:10000]
    games2 = games[10000:20000]
    games3 = games[20000:30000]
    games4 = games[30000:40000]
    games5 = games[40000:]
    all_games = [games1, games2, games3, games4, games5]
    for games2 in all_games:
        documents = []
        for game in games2:
            document1: GameSearchObject = GameSearchObject.from_game(game)
            documents.append(document1.__dict__)
        result = search_client.upload_documents(documents=documents)
        print("Upload of new document succeeded: {}".format(
            result[0].succeeded))
