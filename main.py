
# from database import GamesDatabase
# from bootstrap import bootstrap
from chroma import ChromaEmbedding
from game import get_games, get_games_from_database, get_complaints_from_database


if __name__ == '__main__':
    # bootstrap()
    games = get_complaints_from_database()
    for game in games:
        # game.orders
        print(game.to_json())

        # print(ll)
    # chroma = ChromaEmbedding()
    # games = get_games()
    # for game in games:
    #     print(game.url)
    #     ll = chroma.create_embedding(game.to_json(), game.url)
    #     # print(ll)
    # ll = chroma.create_embedding_only('hello world')
    # print(ll)
    # print('Hello World!')
    # games = get_games()
    # save_games(games=games)
    # db = GamesDatabase()
    # print('connect to database')
    # for game in games:
    #     db.insert_game(game)

    # print('inserted games into database')
