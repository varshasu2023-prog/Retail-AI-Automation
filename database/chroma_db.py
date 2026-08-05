from langchain_chroma import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings
import streamlit as st


def create_vector_db(chunks):

    embeddings = GoogleGenerativeAIEmbeddings(
        model="models/embedding-001",
        google_api_key=st.secrets["GEMINI_API_KEY"]
    )

    vector_db = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings
    )

    return vector_db
