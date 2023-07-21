
from Actions.actions import ActionsEnum, ChatBotAction, GetAction


def begin_chat_bot():
    """Main entrypoint in the chatbot workflow."""
    entry_level: ChatBotAction = ""
    while True:
        actions_enum = entry_level.execute()
        if actions_enum == ActionsEnum.End:
            break
        else:
            entry_level = GetAction(actions_enum)
