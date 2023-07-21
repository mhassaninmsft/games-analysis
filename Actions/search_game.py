
from Actions.actions import ActionsEnum, ChatBotAction
from chat_bot import ChatBot
from game_search import GameSearch
import json

# should be checked from the AI response
adding_game_key_word = "Trying to Add Game"
restart_over = "Restart Over"  # Should be checked at user side

# read the system prompt from file "GameSearchPrompt.txt"
system_prompt = ""
with open("./Prompts/GameSearchPrompt.txt", "r") as f:
    system_prompt = f.read()


class GameSearchAction(ChatBotAction):
    def __init__(self, games_query: str):
        self.games_query = games_query
        self.gameSearch = GameSearch()
        initial_games = self.gameSearch.search_game(games_query)
        system_message = f"{system_prompt} and here is the list of games {str(initial_games)}"
        self.chat_bot = ChatBot(system_message=system_message)

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
                return ActionsEnum.End

                # return ActionsEnum.AddGame
