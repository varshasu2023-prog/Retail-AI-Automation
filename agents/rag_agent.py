from models.llm import get_llm


def generate_answer(vector_db, question):

    llm = get_llm()

    retriever = vector_db.as_retriever(
        search_kwargs={"k":3}
    )

    documents = retriever.invoke(question)

    context = "\n".join(
        doc.page_content for doc in documents
    )

    prompt = f"""
    Use this information to answer.

    Context:
    {context}

    Question:
    {question}
    """

    response = llm.invoke(prompt)

    return response.content
