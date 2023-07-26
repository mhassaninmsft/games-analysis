
from Actions.actions import ActionsEnum, ChatBotAction
from Actions.checkout import CheckoutAction
from Actions.complaint import ComplaintAction
from Actions.search_faq import SearchFaqAction
from Actions.search_game import GameSearchAction
from chat_bot import ChatBot

# read the system prompt from file "GameSearchPrompt.txt"
system_prompt = ""
with open("./Prompts/BasePrompt.txt", "r") as f:
    system_prompt = f.read()


def get_entry_point(first_user_msg: str) -> ChatBotAction:
    """ Get the entry point for the workflow."""
    # use your prompt to determine the workflow
    chat_bot = ChatBot(system_message=system_prompt)
    response = chat_bot.add_chatbot_message(first_user_msg)
    print("Chatbot: " + response)
    # Parse response string into ActionEnum
    response_enum = ActionsEnum(response)
    if response_enum == ActionsEnum.ProductSearchOrPurchase:
        return GameSearchAction(first_user_msg)
    elif response_enum == ActionsEnum.Complaint:
        return ComplaintAction(complaint=first_user_msg)
    elif response_enum == ActionsEnum.CheckOut:
        return CheckoutAction()
    elif response_enum == ActionsEnum.FaQSearch:
        return SearchFaqAction(first_user_msg)
    elif response_enum == ActionsEnum.End:
        print("Ending Conversation")
    else:
        raise Exception(f"Invalid action received {response}")
    pass
