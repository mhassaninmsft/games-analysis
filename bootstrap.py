# This script is used to bootstrap the project. It will read the list
# of games from the CSV file
# Write to a PostgreSQL database, also for each game it will create an
# embedding against OPENAI

from game import get_games, save_games


def bootstrap():
    """ This function will read the list of games from the CSV file and return
      a list of Game objects"""
    games = get_games()
    save_games(games)
