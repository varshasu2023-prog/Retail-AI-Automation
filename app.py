import streamlit as st
import streamlit as st

from agents.rag_agent import generate_answer
from utils.pdf_loader import load_pdf
from utils.text_splitter import split_documents
from database.chroma_db import create_vector_db

st.set_page_config(
    page_title="Retail AI Automation",
    page_icon="🛍️",
    layout="wide"
)

st.title("🛍️ Retail AI Automation")
st.subheader("AI-Powered Retail Document Assistant")

# Sidebar
with st.sidebar:
    st.header("⚙️ Options")

    option = st.selectbox(
        "Choose Action",
        [
            "Ask Question",
            "Summarize Document",
            "Product Analysis",
            "Inventory Analysis"
        ]
    )

    st.divider()

    st.info(
        """
        Upload a retail PDF and ask AI questions.

        Examples:
        - What is the top selling product?
        - Which product has low stock?
        - Explain customer reviews
        """
    )


# Upload PDF
uploaded_file = st.file_uploader(
    "📄 Upload a Retail PDF",
    type=["pdf"]
)


# Question box
question = st.text_input(
    "💬 Ask a question about the document"
)


# Example questions
st.write("### 💡 Example Questions")

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("📦 Show products"):
        question = "List all products"

with col2:
    if st.button("📊 Sales summary"):
        question = "Give sales summary"

with col3:
    if st.button("⚠️ Low stock items"):
        question = "Which products have low stock?"


# Ask button
if st.button("🚀 Ask AI"):

    if uploaded_file is None:
        st.warning("Please upload PDF")

    elif question == "":
        st.warning("Please enter question")

    else:

        st.success("✅ PDF processed successfully")

        answer = generate_answer(
            vector_db,
            question
        )

        st.subheader("🤖 AI Answer")

        st.write(answer)


# Footer
st.divider()

st.caption(
    "Built with LangChain + ChromaDB + Gemini + Streamlit"
)
