# This handles both the generic product compalint but only if the user has purchased the product.
# Also handles the generic complaint about perhaps the website or the service.


from Actions.actions import ActionsEnum, ChatBotAction
from chat_bot import ChatBot
from models import DbConnection
from globals import user_id

# read the system prompt from file "GameSearchPrompt.txt"
system_prompt = ""
with open("./Prompts/GameSearchPrompt.txt", "r") as f:
    system_prompt = f.read()


class ComplaintAction(ChatBotAction):
    def __init__(self, complaint: str):
        self.db_connection = DbConnection()
        self.complaint = complaint
        self.chat_bot = ChatBot(system_message=complaint)
        self.user_id = user_id

    def execute(self) -> ActionsEnum:
        """Main entrypoint in the chatbot workflow."""
        # Initially we use the game_query as the user message
        begin = True
        while True:
            if begin:
                user_message = self.complaint
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
