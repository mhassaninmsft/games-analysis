
from Actions.actions import ActionsEnum, ChatBotAction, GetAction
from Actions.search_game import GameSearchAction


def begin_chat_bot():
    """Main entrypoint in the chatbot workflow."""
    current_action: ChatBotAction = GameSearchAction(
        games_query="I am looking to buy a game about dragons")
    while True:
        current_action = current_action.execute()
        if current_action == ActionsEnum.End:
            break
        else:
            print("Domryjinh new returned")
            # current_action = GetAction(current_action)
