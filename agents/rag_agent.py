from langchain_google_genai import ChatGoogleGenerativeAI
import streamlit as st


def generate_answer(vector_db, question):

    docs = vector_db.similarity_search(
        question,
        k=3
    )

    context = "\n\n".join(
        [doc.page_content for doc in docs]
    )


    llm = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        google_api_key=st.secrets["GEMINI_API_KEY"],
        temperature=0.3
    )


    prompt = f"""
You are a retail AI assistant.

Use the following document context to answer the question.

Context:
{context}

Question:
{question}

Answer clearly:
"""


    response = llm.invoke(prompt)

    return response.content
