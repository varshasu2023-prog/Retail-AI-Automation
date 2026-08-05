from langchain_google_genai import ChatGoogleGenerativeAI
import streamlit as st


def generate_answer(vector_db, question):

    docs = vector_db.similarity_search(question, k=3)

    context = "\n\n".join(
        [doc.page_content for doc in docs]
    )

    llm = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash-lite",
        google_api_key=st.secrets["GEMINI_API_KEY"],
        temperature=0
    )

    prompt = f"""
You are a retail document assistant.

Answer only using this context:

{context}

Question:
{question}
"""

    response = llm.invoke(prompt)

    return response.content

