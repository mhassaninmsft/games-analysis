
# from pydantic import BaseModel
from LangChain.lang_chain_integration import run_tool
from bootstrap import bootstrap
from Actions.workflow import begin_chat_bot
from fulltextsearch.add_documents import add_documents
from fulltextsearch.create_index import bootstrap_index
from fulltextsearch.search_documents import search_for_documents
from game_search import GameSearch, example_usage
from Actions.actions import ActionsEnum
import asyncio

from models import Game

from dataclasses import dataclass
from dataclasses_json import dataclass_json

from web_server.entry_point import start_server


# Creating a Game object
# game = Game(id="123", similarity=0.2, result_text="Sample Result Text")

if __name__ == '__main__':
    # bootstrap()
    # begin_chat_bot()
    # bootstrap_index()
    # add_documents()
    # run_tool()
    start_server()
    # search_for_documents("Tomb Raider")
    # print(game)
