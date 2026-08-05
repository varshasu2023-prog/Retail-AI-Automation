from langchain_chroma import Chroma
from utils.embeddings import get_embedding

DB_PATH = "vector_db/chroma_db"

def create_vector_store(documents):
    db = Chroma.from_documents(
        documents=documents,
        embedding=get_embedding(),
        persist_directory=DB_PATH
    )

    return db


def load_vector_store():
    db = Chroma(
        persist_directory=DB_PATH,
        embedding_function=get_embedding()
    )

    return db
