from langchain_google_genai import ChatGoogleGenerativeAI
import streamlit as st


def generate_answer(vector_db, question):

    llm = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        google_api_key=st.secrets["GEMINI_API_KEY"]
    )

    response = llm.invoke("Explain retail in one sentence")

    return response.content
