from chromadb.config import Settings
import chromadb
# import uuid

# collection = client.get_collection(name="my_collection")


class ChromaEmbedding:
    """ Chroma Embedding """
    # client: chromadb.Client
    # collection: chromadb.Collection

    def __init__(self, collection_name: str = "my_collection"):
        self.client = chromadb.Client(Settings(
            chroma_db_impl="duckdb+parquet",
            # Optional, defaults to .chromadb/ in the current directory
            # persist_directory="/mnt/chromastate/chromastate/"
            persist_directory="./chromastate/"
        ))
        # self.client = chromadb.PersistentClient(
        #     path="/mnt/chromastate/chromastate")
        self.collection = self.client.get_or_create_collection(
            name=collection_name)

    def create_embedding(self, inputText, id: str):
        """ Create an embedding from a text. Here the id is the url
        of the website"""
        self.collection.add(
            documents=[inputText],
            # By removing the embedding we use the default embedding function
            # embeddings=[inputEmbedding],
            # metadatas=[{"chapter": "3", "verse": "16"}, {
            # "chapter": "3", "verse": "5"}, {"chapter": "29", "verse": "11"},
            #  ...],
            ids=[id]
        )

    def search_by_embedding(self, embedding):
        """ Search for an embedding by query."""
        res = self.collection.query(
            query_embeddings=[embedding],
            n_results=10,
            # where={"metadata_field": "is_equal_to_this"},
            # where_document={"$contains": "search_string"}
        )
        print(res)
        return res

    def create_embedding_only(self, text: str):
        print("hello")
        embs = self.collection._embedding_function([text])
        v = embs[0]
        print(v)
        return v

    def get_version(self):
        return self.client.get_version()
        """ Get the version of ChromaDB."""
