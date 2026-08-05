from langchain_chroma import Chroma
from utils.embeddings import get_embedding

DB_PATH = "vector_db/chroma_db"

def save_documents(documents):

    db = Chroma.from_documents(
        documents=documents,
        embedding=get_embedding(),
        persist_directory=DB_PATH
    )

    return db

def load_database():

    return Chroma(
        persist_directory=DB_PATH,
        embedding_function=get_embedding()
    )
