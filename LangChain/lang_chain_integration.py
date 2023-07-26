# Import things that are needed generically
import datetime
from globals import user_id
from langchain.callbacks.manager import (
    AsyncCallbackManagerForToolRun,
    CallbackManagerForToolRun,
)
from typing import Optional, Type
from langchain import LLMMathChain, SerpAPIWrapper
from langchain.agents import AgentType, initialize_agent
from langchain.chat_models import ChatOpenAI
from langchain.tools import BaseTool, StructuredTool, Tool, tool

from Actions.complaint import ComplaintAction, GamePurchased
from models import Complaint, DbConnection, Game, Purchase
llm = ChatOpenAI(temperature=0)


class ComplaintTool(BaseTool):
    name = "ComplaintTool"
    description = "useful for when you the user needs to make a complaint about a product or service."

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user_id = user_id
        self.db_connection = DbConnection()
        user_games = self.get_purchased_games_by_user()

    def _run(
        self,
        query: str,
        run_manager: Optional[CallbackManagerForToolRun] = None,
    ) -> str:
        """Use the tool."""
        complaint_action = ComplaintAction(query)
        return str(complaint_action.execute())
        # search_wrapper = SerpAPIWrapper(
        #     params={"engine": engine, "gl": gl, "hl": hl})
        # return search_wrapper.run(query)

    # async def _arun(
    #     self,
    #     query: str,
    #     engine: str = "google",
    #     gl: str = "us",
    #     hl: str = "en",
    #     run_manager: Optional[AsyncCallbackManagerForToolRun] = None,
    # ) -> str:
    #     """Use the tool asynchronously."""
    #     raise NotImplementedError("custom_search does not support async")


@tool
def get_purchased_games_by_user() -> list[GamePurchased]:
    """ This function retrieves the list of game ids, names and descriptions that a particular user has purchased. 

    Returns:
        list[GamePurchased]: A list of GamePurchased, where each GamePurchased contains the game name and description for each game purchased by the user.
    """
    db_connection = DbConnection()
    session = db_connection.get_session()
    purchases = session.query(Purchase).filter(
        Purchase.customer_id == user_id).all()

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
