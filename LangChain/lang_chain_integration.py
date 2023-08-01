# Import things that are needed generically
import datetime

from pydantic import BaseModel, Field
from Actions.checkout import CheckoutAction
from faq_embeddings import FaQEmbedding
from game_search import GameSearch
from globals import user_id
# from langchain.callbacks.manager import (
#     AsyncCallbackManagerForToolRun,
#     CallbackManagerForToolRun,
# )
from typing import Optional, Type
# from langchain import LLMMathChain, SerpAPIWrapper
from langchain.agents import AgentType, initialize_agent
from langchain.chat_models import AzureChatOpenAI
from langchain.tools import BaseTool, StructuredTool, Tool, tool
import langchain
from langchain.memory import ConversationBufferMemory

import os
from Actions.complaint import ComplaintAction, GamePurchased
from models import Complaint, DbConnection, Game, Purchase
from langchain.prompts import MessagesPlaceholder
from Actions.search_game import get_game_by_url, add_game_to_cart
# If you want to trace the execution of the program, set to "true"
# os.environ["LANGCHAIN_TRACING"] = "true"
# os.environ["LANGCHAIN_HANDLER"] = "langchain"

# openai.api_type = "azure"
# openai.api_base = "https://longfellowai.openai.azure.com/"
# openai.api_version = "2023-03-15-preview"
# openai.api_key = os.getenv("OPENAI_API_KEY")

os.environ["OPENAI_API_TYPE"] = "azure"
os.environ["OPENAI_API_VERSION"] = "2023-03-15-preview"
os.environ["OPENAI_API_BASE"] = "https://longfellowai.openai.azure.com/"
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")


langchain.verbose = True

llm = AzureChatOpenAI(temperature=0, deployment_name="gpt67",
                      max_retries=3, request_timeout=30)
# llm = AzureChatOpenAI(temperature=0, deployment_name="gpt353",
#                       max_retries=3, request_timeout=30)


print("LLM Created")


class ComplaintInput(BaseModel):
    purchase_id: int = Field()
    complaint: str = Field()


class AddGameToCartInput(BaseModel):
    game_url: str = Field()


# @tool("get_purchased_games_by_user")


db_connection = DbConnection()
session = db_connection.get_session()


def get_purchased_games_by_user() -> str:
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
            (GamePurchased(game_id=game.id, name=game.name, description="none", purchase_id=purchase.id)))

    return str(purchased_games_info)


# @tool("add_complaint_to_database")
def add_complaint_to_database(purchase_id: int, complaint: str) -> str:
    """This function will add the complaint to the database"""
    print(f"received purchase_id: {purchase_id} and complaint: {complaint}")
    db_connection = DbConnection()
    session = db_connection.get_session()
    complaint = Complaint(
        complaint=complaint, customer_id=user_id, created_at=datetime.datetime.now(), purchase_id=purchase_id)
    session.add(complaint)
    session.commit()
    return "Complaint Added"


# @tool("get_game_purchase_id")
def get_game_purchase_id(game: str) -> int:
    """ """
    print(f"received game: {game}")
    return 1


def checkout_user_cart() -> str:
    print("Shipping address: 123 Main St.")
    checkout_action = CheckoutAction()
    checkout_action.execute()
    return "Checkout Completed"


def get_closest_faq(question: str) -> str:
    my_embeddings_service = FaQEmbedding()
    res = my_embeddings_service.search_faq(question)
    return str(res)


def answer_game_realted_questions(question: str) -> str:
    my_embeddings_service = GameSearch()
    res = my_embeddings_service.search_game(question)
    return str(res)


def add_game_to_cart_action(game_url: str) -> str:
    print(f"received game_url: {game_url}")
    game = get_game_by_url(game_url, session)
    add_game_to_cart(game, session)
    return "Game Added To Cart"


tools = [
    # StructuredTool.from_function(
    #     func=get_purchased_games_by_user,
    #     name="Get User Games",
    #     # args_schema=None,
    #     description="Gets all the user purchased games",
    #     # coroutine= ... <- you can specify an async method if desired as well
    # ),
    StructuredTool.from_function(
        func=add_complaint_to_database,
        name="Add Complaint To Database",
        description="Add a complaint to the database, given a purchase id and a complaint",
        args_schema=ComplaintInput,
        # coroutine= ... <- you can specify an async method if desired as well
    ),
    StructuredTool.from_function(
        func=checkout_user_cart,
        name="Checks out the user cart",
        description="Checks out the user cart",
        # args_schema=ComplaintInput,
        # coroutine= ... <- you can specify an async method if desired as well
    ),

    StructuredTool.from_function(
        func=get_closest_faq,
        name="GetFAQSummary",
        description="returns the relevant FAQ section summary that can be used to answer the user's question",
        # args_schema=ComplaintInput,
        # coroutine= ... <- you can specify an async method if desired as well
    ),

    StructuredTool.from_function(
        func=answer_game_realted_questions,
        name="AnswerGameRelatedQuestions",
        description="returns the list of games that are related to the user's question about games",
        # args_schema=ComplaintInput,
        # coroutine= ... <- you can specify an async method if desired as well
    ),

    StructuredTool.from_function(
        func=add_game_to_cart_action,
        name="AddGameToCart",
        description="Adds the seen game to the user's cart",
        # return_direct=True,
        args_schema=AddGameToCartInput,
        # coroutine= ... <- you can specify an async method if desired as well
    ),

    # StructuredTool.from_function(
    #     func=get_game_purchase_id,
    #     name="Get_Purchase_Id",
    #     description="You can use that tool to look up the game purchase id for a game name."
    #     # coroutine= ... <- you can specify an async method if desired as well
    # ),
]
chat_history = MessagesPlaceholder(variable_name="chat_history")
memory = ConversationBufferMemory(
    memory_key="chat_history", return_messages=True)
# user_games = get_purchased_games_by_user()
# memory.chat_memory.add_user_message(
#     f" The list of my purchased games are{user_games}")
# memory.chat_memory.add_user_message(
#     """ If the user is asking questions from the FAQ, you can use the tool GetFAQSummary to get the
#     relevant section from the FAQ and then answer the user question faithfully, It is important to answer the user question""")


def run_tool():
    # Construct the agent. We will use the default agent type here.
    agent = initialize_agent(
        tools, llm, agent=AgentType.STRUCTURED_CHAT_ZERO_SHOT_REACT_DESCRIPTION, verbose=True, memory=memory,
        agent_kwargs={
            "memory_prompts": [chat_history],
            "input_variables": ["input", "agent_scratchpad", "chat_history"]
        }
    )
    # agent.agent.llm_chain.prompt.template
    # agent.agent.llm_chain.prompt.lc_kwargs["messages"][0].lc_kwargs[
    #     "prompt"].lc_kwargs["template"] += "The Purchase if for the game Doom 2 is 3"
    # print(
    #     agent.agent.llm_chain.prompt.lc_kwargs["messages"][0].lc_kwargs["prompt"].lc_kwargs["template"])

    while True:
        user_input = input("User: ")
        # agent.run(user_input)
        res = agent.run(input=user_input)
        print("Chatbot: " + res)
