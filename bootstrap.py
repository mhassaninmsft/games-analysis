# This script is used to bootstrap the project. It will read the list
# of games from the CSV file
# Write to a PostgreSQL database, also for each game it will create an
# embedding against OPENAI

from chroma import ChromaEmbedding
from embeddings import MyEmbedding
from faq_embeddings import FaQEmbedding
from models import Game, get_games, save_games_to_psql_database


def bootstrap():
    """ This function will read the list of games from the CSV file and save them
      to the database and create embeddings for each game and save them to the
      chroma database"""
    games = get_games()
    # save_games_to_psql_database(games)
    create_and_save_game_embeddings(games)
    # create_and_save_faq_embeddings()


def create_and_save_game_embeddings(games: list[Game]):
    """ This function will save the list of games to the chroma embeddings database"""
    chroma = MyEmbedding(collection_name="games")
    # take first 1000 games for testing
    games = games[25000:30000]
    # 3145
    counter = 25000
    for game in games:
        # print(game.url)
        print(f" game number {counter} and url {game.url}")
        ll = chroma.create_and_save_embedding(game.to_json(), game.url)
        counter = counter+1


# create and save faq embeddings
def create_and_save_faq_embeddings():
    """ This function will save the list of games to the chroma embeddings database"""
    chroma = FaQEmbedding()
    chroma.create_faq_embeddings()
