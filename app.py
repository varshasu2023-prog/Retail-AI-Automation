import streamlit as st
from dotenv import load_dotenv
import os

from utils.pdf_loader import load_pdf
from utils.text_splitter import split_documents
from database.chroma_db import create_vector_db
from agents.rag_agent import generate_answer


load_dotenv()

st.set_page_config(
    page_title="Retail AI Automation",
    page_icon="🛍️",
    layout="wide"
)


st.title("🛍️ Retail AI Automation")
st.write("### AI-Powered Retail Document Assistant")


uploaded_file = st.file_uploader(
    "Upload a Retail PDF",
    type=["pdf"]
)


if uploaded_file:

    # Save PDF temporarily
    with open("temp.pdf", "wb") as f:
        f.write(uploaded_file.getbuffer())


    # Load PDF
    documents = load_pdf("temp.pdf")


    # Split text
    chunks = split_documents(documents)


    # Create ChromaDB
    vector_db = create_vector_db(chunks)


    st.success("✅ PDF uploaded successfully!")


    question = st.text_input(
        "Ask a question about the document"
    )


    if st.button("Ask AI"):

        if question:

            answer = generate_answer(
                vector_db,
                question
            )

            st.write("### AI Answer:")
            st.success(answer)

        else:
            st.warning("Please enter a question.")
