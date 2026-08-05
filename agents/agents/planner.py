from utils.retriever import retrieve
from models.llm import get_llm

def ask_agent(question):

    docs = retrieve(question)

    context = "\n\n".join(
        [doc.page_content for doc in docs]
    )

    prompt = f"""
Answer the question using only the context.

Context:
{context}

Question:
{question}
"""

    llm = get_llm()

    response = llm.invoke(prompt)

    return response.content
