
# from database import GamesDatabase
# from bootstrap import bootstrap
# from chroma import ChromaEmbedding
# from game import get_complaints_from_database
from Actions.workflow import begin_chat_bot
from game_search import GameSearch, example_usage
from Actions.actions import ActionsEnum

if __name__ == '__main__':
    # bootstrap()
    # example_usage()
    begin_chat_bot()
    # action1 = ActionsEnum.Complaint
    # print(str(action1))
    # action2 = ActionsEnum("Inquire2")
    # print(action2)
    # games = get_complaints_from_database()
    # for game in games:
    #     # game.orders
    #     print(game.to_json())

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
