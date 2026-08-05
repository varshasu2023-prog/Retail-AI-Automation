import streamlit as st

from utils.pdf_loader import load_pdf
from utils.text_splitter import split_documents
from database.chroma_db import create_vector_db
from agents.rag_agent import generate_answer


# Page configuration
st.set_page_config(
    page_title="Retail AI Automation",
    page_icon="🛍️",
    layout="wide"
)


# Title
st.title("🛍️ Retail AI Automation")
st.subheader("AI-Powered Retail Document Assistant")

st.markdown("---")


# Sidebar
with st.sidebar:

    st.header("⚙️ Dashboard")

    option = st.selectbox(
        "Choose Analysis Type",
        [
            "Ask Question",
            "Summarize Document",
            "Product Analysis",
            "Inventory Analysis",
            "Sales Analysis"
        ]
    )

    st.markdown("---")

    st.header("💡 Sample Questions")

    st.write(
        """
        - What is the top selling product?
        - Which products have low stock?
        - Explain customer reviews
        - List all products
        - Give sales summary
        """
    )

    st.markdown("---")

    st.info(
        "Powered by:\n\n"
        "LangChain\n"
        "ChromaDB\n"
        "Gemini\n"
        "Streamlit"
    )


# Dashboard metrics
col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "📄 Documents",
        "1"
    )

with col2:
    st.metric(
        "🔍 AI Engine",
        "Active"
    )

with col3:
    st.metric(
        "🗄️ Vector DB",
        "ChromaDB"
    )


st.markdown("---")


# PDF Upload

st.header("📄 Upload Retail Document")


uploaded_file = st.file_uploader(
    "Upload a Retail PDF",
    type=["pdf"]
)


vector_db = None


if uploaded_file:

    with open("temp.pdf", "wb") as f:
        f.write(uploaded_file.getbuffer())


    with st.spinner("Processing PDF..."):

        documents = load_pdf("temp.pdf")

        chunks = split_documents(documents)

        vector_db = create_vector_db(chunks)


    st.success(
        "✅ PDF uploaded and processed successfully!"
    )



st.markdown("---")


# Question section

st.header("💬 Ask AI About Your Document")


question = st.text_input(
    "Enter your question"
)



# Quick buttons

st.write("### 🚀 Quick Actions")


c1, c2, c3, c4 = st.columns(4)


with c1:
    if st.button("📦 Products"):
        question = "List all products"


with c2:
    if st.button("📊 Sales"):
        question = "Give sales summary"


with c3:
    if st.button("⚠️ Low Stock"):
        question = "Which products have low stock?"


with c4:
    if st.button("⭐ Reviews"):
        question = "Summarize customer reviews"



# Ask AI button

if st.button("🤖 Generate AI Answer"):


    if vector_db is None:

        st.warning(
            "Please upload a PDF first"
        )


    elif question == "":

        st.warning(
            "Please enter a question"
        )


    else:

        with st.spinner("AI is thinking..."):

            answer = generate_answer(
                vector_db,
                question
            )


        st.success(
            "Answer Generated"
        )


        st.subheader(
            "🤖 AI Answer"
        )


        st.write(answer)



st.markdown("---")


st.caption(
    "🛍️ Retail AI Automation | LangChain + ChromaDB + Gemini + Streamlit"
)

