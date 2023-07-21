
from chroma import ChromaEmbedding
from game import get_games_from_database_by_url
# from csvReader import get_data
# import uuid


class GameSearch:
    def __init__(self) -> None:
        collection_name = "my_collection"
        self.chroma_embedding = ChromaEmbedding(
            collection_name=collection_name)

    def search_game(self, request: str):
        """ Search the FAQ for the request."""
        embedding = self.chroma_embedding.create_embedding_only(request)
        return self.get_closest_match(embedding)

    def get_closest_match(self, embedding):
        """ Get the closest match to the embedding."""
        return self.chroma_embedding.search_by_embedding(embedding=embedding)

    # TODO: Add a full text search using either


def example_usage():
    gameSearch = GameSearch()
    games = gameSearch.search_game('Kingdom Come')
    for id in games['ids']:
        for id1 in id:
            game = get_games_from_database_by_url(id1)
            print(game[0].name)
            print(id1)
