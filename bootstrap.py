# This script is used to bootstrap the project. It will read the list
# of games from the CSV file
# Write to a PostgreSQL database, also for each game it will create an
# embedding against OPENAI

from chroma import ChromaEmbedding
from models import Game, get_games, save_games_to_psql_database


def bootstrap():
    """ This function will read the list of games from the CSV file and save them
      to the database and create embeddings for each game and save them to the
      chroma database"""
    games = get_games()
    save_games_to_psql_database(games)
    create_and_save_embeddings(games)


def create_and_save_embeddings(games: list[Game]):
    """ This function will save the list of games to the chroma embeddings database"""
    chroma = ChromaEmbedding()
    for game in games:
        print(game.url)
        ll = chroma.create_embedding(game.to_json(), game.url)
