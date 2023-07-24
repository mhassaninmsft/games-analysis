# This handles both the generic product compalint but only if the user has purchased the product.
# Also handles the generic complaint about perhaps the website or the service.


import datetime
from Actions.actions import ActionsEnum, ChatBotAction
from chat_bot import ChatBot
from models import Complaint, DbConnection, Game, ShoppingCart
from game_search import GameSearch
import json
from globals import user_id
from sqlalchemy.orm import Session


class ComplaintAction(ChatBotAction):
    def __init__(self, user_complaint_query: str):

        self.db_connection = DbConnection()
        pass

    def execute(self) -> ActionsEnum:
        """Main entrypoint in the Complaint workflow."""
        session = self.db_connection.get_session()
        complaint = input("Please enter your complaint: ")
        purchase_id = input("Please enter your purchase id: ")
        complaint = Complaint(complaint=complaint, customer_id=user_id, purchase_id=purchase_id,
                              created_at=datetime.datetime.now())
        session.add(complaint)
        session.commit()
        return ActionsEnum.End
