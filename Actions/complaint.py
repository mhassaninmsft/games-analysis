# This handles both the generic product compalint but only if the user has purchased the product.
# Also handles the generic complaint about perhaps the website or the service.

from dataclasses import dataclass
import datetime
import json

from dataclasses_json import dataclass_json
from Actions.actions import ActionsEnum, ChatBotAction
from chat_bot import ChatBot
from models import DbConnection, Game, Purchase, Complaint
from globals import user_id

# read the system prompt from file "GameSearchPrompt.txt"
system_prompt = ""
with open("./Prompts/CompalintPrompt.txt", "r") as f:
    system_prompt = f.read()


@dataclass_json
@dataclass
class GamePurchased:
    """This class represents a game that has been purchased by a user."""
    game_id: int
    name: str
    description: str
    purchase_id: int


class ComplaintAction(ChatBotAction):
    def __init__(self, complaint: str):
        self.user_id = user_id
        self.db_connection = DbConnection()
        user_games = self.get_purchased_games_by_user()
        print(f"User Games: {user_games}")
        self.complaint = complaint
        system_message = system_prompt.format(products=user_games)
        print(system_message)
        self.chat_bot = ChatBot(system_message=system_message)

    def execute(self) -> ActionsEnum:
        """Main entrypoint in the chatbot workflow."""
        # Initially we use the game_query as the user message
        user_message = self.complaint
        res = self.chat_bot.add_chatbot_message(user_message)
        print(f"raw response from chatbot: {res}")
        # Convert message to JSON
        res_json = json.loads(res)
        print(f"json from chatbot: {res_json}")
        if res_json['type'] == "ProductComplaint":
            purchase_id = res_json["purchase_id"]
            self.add_complaint_to_database(purchase_id)
            print("Chatbot: Product Complaint. Thank you for letting us know.")
        elif res_json["type"] == "GeneralComplaint":
            print("Chatbot: General Complaint. Thank you for letting us know.")
        elif res_json["type"] == "NotPurchased":
            print(
                "Chatbot: You have Not Purchased this game. Thank you for letting us know.")
        return ActionsEnum.End

    def get_purchased_games_by_user(self) -> list[GamePurchased]:
        """ This function retrieves the list of game ids, names and descriptions that a particular user has purchased. 

        Returns:
            list[GamePurchased]: A list of GamePurchased, where each GamePurchased contains the game name and description for each game purchased by the user.
        """
        session = self.db_connection.get_session()
        purchases = session.query(Purchase).filter(
            Purchase.customer_id == self.user_id).all()

        purchased_games_info = []
        for purchase in purchases:
            game = session.query(Game).filter(
                Game.id == purchase.game_id).one()
            purchased_games_info.append(
                (GamePurchased(game_id=game.id, name=game.name, description=game.game_description, purchase_id=purchase.id)))

        return purchased_games_info

    def add_complaint_to_database(self, purchase_id: int):
        session = self.db_connection.get_session()

        complaint = Complaint(
            complaint=self.complaint, customer_id=self.user_id, created_at=datetime.datetime.now(), purchase_id=purchase_id)
        session.add(complaint)
        session.commit()
