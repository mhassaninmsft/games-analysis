
from Actions.actions import ActionsEnum, ChatBotAction, GetAction
from Actions.checkout import CheckoutAction
from Actions.search_game import GameSearchAction


def begin_chat_bot():
    """Main entrypoint in the chatbot workflow."""
    # current_action: ChatBotAction = GameSearchAction(
    #     games_query="I am looking to buy a REAL time strategy game")
    current_action: ChatBotAction = CheckoutAction()
    while True:
        current_action = current_action.execute()
        if current_action == ActionsEnum.End:
            print("Ending Conversation")
            break
        else:
            print("Domryjinh new returned")
            # current_action = GetAction(current_action)
