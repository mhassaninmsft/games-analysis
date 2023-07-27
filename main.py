
# from pydantic import BaseModel
from LangChain.lang_chain_integration import run_tool
from bootstrap import bootstrap
from Actions.workflow import begin_chat_bot
from game_search import GameSearch, example_usage
from Actions.actions import ActionsEnum
import asyncio

# from langchain.experimental import BabyAGI


# class BabyAGI(Chain, BaseModel):
#     """Controller model for the BabyAGI agent."""

#     # Other class code...

#     class Config:
#         """Configuration for this pydantic object."""

#         arbitrary_types_allowed = True


if __name__ == '__main__':
    # bootstrap()
    # begin_chat_bot()
    run_tool()
