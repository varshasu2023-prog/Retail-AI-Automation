from langchain_chroma import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings
import streamlit as st


def create_vector_db(chunks):

    embeddings = GoogleGenerativeAIEmbeddings(
        model="models/text-embedding-004",
        google_api_key=st.secrets[AIzaSyAb8RN6I7RQHMvBdDRMwYLep_D6n0MCY0wvDOvq9Qg0Nq1TAaKA]
    )

    vector_db = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory="chroma_db"
    )

    return vector_db
