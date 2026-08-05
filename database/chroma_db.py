from langchain_chroma import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings


def create_database(chunks):

    embeddings = GoogleGenerativeAIEmbeddings(
        model="models/embedding-001"
    )

    vector_db = Chroma.from_documents(
        chunks,
        embeddings,
        persist_directory="chroma_db"
    )

    return vector_db
