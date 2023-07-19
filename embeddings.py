
import os
import openai
from chroma import ChromaEmbedding
openai.api_type = "azure"
openai.api_base = "https://longfellowai.openai.azure.com/"
openai.api_version = "2023-03-15-preview"
openai.api_key = os.getenv("OPENAI_API_KEY")


class MyEmbedding:
    def __init__(self):
        pass

    def create_and_save_embedding(self, input):
        """ Create an embedding from a text string. and saves it to a vector
          database"""
        response = openai.Embedding.create(
            input=input,
            engine="adaembedding1")
        embeddings = response['data'][0]['embedding']
        chroma_db = ChromaEmbedding()
        chroma_db.create_embedding(input, embeddings)
        print(response)

    def search_by_embedding(self, embedding):
        """ Search for an embedding by query."""
        chroma_db = ChromaEmbedding()
        return chroma_db.search_by_embedding(embedding)

    def create_embedding(self, input):
        """ Create an embedding from a text string."""
        response = openai.Embedding.create(
            input=input,
            engine="adaembedding1")
        embeddings = response['data'][0]['embedding']
        return embeddings

    # def search(self, query):
    #     """ Search for an embedding by query."""
    #     chroma_db = ChromaEmbedding()
    #     chroma_db
