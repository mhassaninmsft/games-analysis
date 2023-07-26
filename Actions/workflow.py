
from Actions.actions import ActionsEnum, ChatBotAction, GetAction
from Actions.base_workflow import get_entry_point
from Actions.checkout import CheckoutAction
from Actions.complaint import ComplaintAction
from Actions.search_faq import SearchFaqAction
from Actions.search_game import GameSearchAction


def begin_chat_bot():
    """Main entrypoint in the chatbot workflow."""
    while True:
        print("Chatbot: How can I be of Assistance to you today? You can browse our lists of games , give us feedback or checkout your cart. \n")
        user_input = input("User: ")
        current_action: ChatBotAction = get_entry_point(user_input)
        current_action = current_action.execute()
        if current_action == ActionsEnum.End:
            print("Successfully Ended Conversation thread, starting new thread")
        else:
            print("Successfully Ended Conversation thread, starting new thread")
