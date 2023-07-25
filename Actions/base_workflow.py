
from Actions.actions import ActionsEnum, ChatBotAction
from Actions.checkout import CheckoutAction
from Actions.complaint import ComplaintAction
from Actions.search_faq import SearchFaqAction
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
    # Parse response string into ActionEnum
    response_enum = ActionsEnum(response)
    if response_enum == ActionsEnum.SearchGame:
        return SearchFaqAction(first_user_msg)
    elif response_enum == ActionsEnum.Complaint:
        return ComplaintAction(first_user_msg)
    elif response_enum == ActionsEnum.CheckOut:
        return CheckoutAction(first_user_msg)
    elif response_enum == ActionsEnum.FaQSearch:
        return FaQSearchAction(first_user_msg)
    elif response_enum == ActionsEnum.End:
        return EndAction(first_user_msg)
    else:
        raise Exception("Invalid action")
    pass
