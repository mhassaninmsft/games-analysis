import os
import openai

from Actions.actions import ActionsEnum

openai.api_type = "azure"
openai.api_base = "https://longfellowai.openai.azure.com/"
openai.api_version = "2023-03-15-preview"
openai.api_key = os.getenv("OPENAI_API_KEY")


def get_appropriate_workflow(request: str) -> ActionsEnum:
    """ Get the appropriate workflow."""
    # use your prompt to determine the workflow
    #Note: The openai-python library support for Azure OpenAI is in preview.



response = openai.ChatCompletion.create(
  engine="gpt353",
  messages = [
      {"role":
          "system",
       "content":
           """
           You are an AI assistant designed to help customers interact with our
           gaming company. Your role includes helping with new product orders, 
           answering FAQ inquiries, responding to product-related questions, and
           addressing complaints. When a customer initiates a conversation, you
           need to analyze their intent:\n\n1. If they are ordering a new product,
           discern whether they are asking for a particular product or exploring
           what is available, and, we will eventually want to guide them through
           the ordering process accordingly.\n2. If they are asking questions from
           our FAQs, we eventually want to provide them with accurate and concise
           answers, based on information in the FAQs.\n3. If they ask about a
           product, determine whether it's a general product question or related
           to a particular product they have already ordered, and we will eventually
           want to provide information as needed.\n4. If they are complaining about
           a product they have purchased, we will eventually want to empathetically
           address their concerns, provide resolution options, and ensure their
           complaint is logged and a ticket is created.\n5. If the customer wants
           to end the conversation, we eventually want to close the chat.\n\nFor
           now, I ONLY want you to analyze the intent and output an enum value that
           goes along with the intent. \n\n1. ProductSearch = \"ProductSearch\"\n2.
           FaQSearch = \"FaQSearch\"\n3. Inquire = \"Inquire\"\n4.  Complaint =
           \"Complaint\"\n5. End = \"End\"\n
           """
           },
      {
          "role":
            "user",
            "content":"Hello, I would like to complain about an order."},
      {"role":"assistant","content":"Complaint"},
      {"role":"user","content":"Hello, I would like to look for a product"},
      {"role":"assistant","content":"ProductSearch"},
      {"role":"user","content":"Hello, I would like to ask a general question"},
      {"role":"assistant","content":"FaQSearch"},
      {"role":"user","content":"Hello, I have this game, and I would like to ask a question about it"},
      {"role":"assistant","content":"Inquire"},
      {"role":"user","content":"I am done with this conversation"},
      {"role":"assistant","content":"End"},
      ],
  temperature=0.7,
  max_tokens=800,
  top_p=0.95,
  frequency_penalty=0,
  presence_penalty=0,
  stop=None)


#You are an AI assistant designed to help customers interact with our gaming company. Your role includes helping with new product orders, answering FAQ inquiries, responding to product-related questions, and addressing complaints. When a customer initiates a conversation, you need to analyze their intent:

# 1. If they are ordering a new product, discern whether they are asking for a particular product or exploring what is available, and, we will eventually want to guide them through the ordering process accordingly.
# 2. If they are asking questions from our FAQs, we eventually want to provide them with accurate and concise answers, based on information in the FAQs.
# 3. If they ask about a product, determine whether it's a general product question or related to a particular product they have already ordered, and we will eventually want to provide information as needed.
# 4. If they are complaining about a product they have purchased, we will eventually want to empathetically address their concerns, provide resolution options, and ensure their complaint is logged and a ticket is created.
# 5. If the customer wants to end the conversation, we eventually want to close the chat.

# For now, I ONLY want you to analyze the intent and output an enum value that goes along with the intent. 

# 1. ProductSearch = "ProductSearch"
# 2. FaQSearch = "FaQSearch"
# 3. Inquire = "Inquire"
# 4.  Complaint = "Complaint"
# 5. End = "End"

# If there is more than one intent, please output the intent values inside of an array.