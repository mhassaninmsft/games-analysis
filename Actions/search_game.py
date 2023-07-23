
from Actions.actions import ActionsEnum, ChatBotAction
from chat_bot import ChatBot
from models import DbConnection, Game, ShoppingCart
from game_search import GameSearch
import json
from globals import user_id
from sqlalchemy.orm import Session
# should be checked from the AI response
adding_game_key_word = "Trying to Add Game"
restart_over = "Restart Over"  # Should be checked at user side

# read the system prompt from file "GameSearchPrompt.txt"
system_prompt = ""
with open("./Prompts/GameSearchPrompt.txt", "r") as f:
    system_prompt = f.read()


class GameSearchAction(ChatBotAction):
    def __init__(self, games_query: str):
        self.db_connection = DbConnection()
        self.games_query = games_query
        self.gameSearch = GameSearch()
        initial_games = self.gameSearch.search_game(games_query)
        system_message = f"{system_prompt} and here is the list of games {str(initial_games)}"
        self.chat_bot = ChatBot(system_message=system_message)
        self.user_id = user_id

    def execute(self) -> ActionsEnum:
        """Main entrypoint in the chatbot workflow."""
        # Initially we use the game_query as the user message
        begin = True
        while True:
            if begin:
                user_message = self.games_query
                begin = False
            else:
                # Then we use the user input as the user message
                user_message = input("User: ")
            # Check if user message contains the restart_over phrase
            if restart_over in user_message:
                print("Ending Conversation")
                return ActionsEnum.End
            response_text = self.chat_bot.add_chatbot_message(user_message)
            print("Chatbot: " + response_text)
            # Check if user message contains the adding_game_key_word phrase
            if adding_game_key_word.lower() in response_text.lower():
                print("Adding Game")
                # Parse the Json response_text
                res = json.loads(response_text)
                print(res)
                game_url = res["cart"][0]["id"]
                print(f"Game: {game_url}")
                session = self.db_connection.get_session()
                game = get_game_by_url(game_url, session)
                print(f"Obtained game from database as {game.name}")
                add_game_to_cart(game, session)
                print("Added game to cart")
                # Add the game to the user cart
                return ActionsEnum.End

                # return ActionsEnum.AddGame


def get_game_by_url(game_url: str, session: Session) -> Game:
    """This function will return a game object from the database based on the game url"""
    game = session.query(Game).filter(Game.url == game_url).first()
    return game


def add_game_to_cart(game: Game, session: Session):
    """This function will add the game to the user cart"""
    user_cart: ShoppingCart = ShoppingCart(
        customer_id=user_id, game_id=game.id)
    session.add(user_cart)
    session.commit()
