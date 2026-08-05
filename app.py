import streamlit as st
from dotenv import load_dotenv
import os

# Load API key from .env
load_dotenv()

st.set_page_config(
    page_title="Retail AI Automation",
    page_icon="🛍️",
    layout="wide"
)

st.title("🛍️ Retail AI Automation")
st.write("### AI-Powered Retail Document Assistant")

api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    st.error("❌ GOOGLE_API_KEY not found. Please add it to your .env file.")
    st.stop()

uploaded_file = st.file_uploader(
    "Upload a Retail PDF",
    type=["pdf"]
)

question = st.text_input(
    "Ask a question about the document"
)

if st.button("Ask AI"):
    if uploaded_file is None:
        st.warning("Please upload a PDF.")
    elif question == "":
        st.warning("Please enter a question.")
    else:
        st.success("✅ PDF uploaded successfully!")
        st.write("Question:", question)

        # This will be replaced later with the RAG pipeline
        st.info("AI response will appear here after we connect LangChain + ChromaDB + Gemini.")
