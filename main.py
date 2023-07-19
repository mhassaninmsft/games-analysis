
# from database import GamesDatabase
from chroma import ChromaEmbedding
# from game import get_games, save_games


if __name__ == '__main__':
    chroma = ChromaEmbedding()
    ll = chroma.create_embedding_only('hello world')
    print(ll)
    # print('Hello World!')
    # games = get_games()
    # save_games(games=games)
    # db = GamesDatabase()
    # print('connect to database')
    # for game in games:
    #     db.insert_game(game)

    # print('inserted games into database')
