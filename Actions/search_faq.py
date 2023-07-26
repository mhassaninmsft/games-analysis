
from Actions.actions import ActionsEnum, ChatBotAction
from chat_bot import ChatBot
from faq_embeddings import FaQEmbedding

# read the system prompt from file "GameSearchPrompt.txt"
system_prompt = ""
with open("./Prompts/FaqPrompt.txt", "r") as f:
    system_prompt = f.read()


class SearchFaqAction():
    def __init__(self, request: str) -> None:
        self.search_faq_service = FaQEmbedding()
        self.request = request
        faq = self.get_closest_docs()
        system_message = system_prompt.format(faq=faq, question=request)
        print(system_message)
        self.chat_bot = ChatBot(system_message=system_message)

    def get_closest_docs(self):
        """ Search the FAQ for the request."""
        docs = self.search_faq_service.search_faq(self.request)
        return docs

    def execute(self) -> ActionsEnum:
        """ Execute the action."""
        res = self.chat_bot.add_chatbot_message(self.request)
        print(f"Chatbot: {res}")
        return ActionsEnum.End
        pass
