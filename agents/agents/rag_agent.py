from models.llm import get_llm


def ask_question(vector_db, question):

    llm = get_llm()

    retriever = vector_db.as_retriever(
        search_kwargs={"k":3}
    )

    docs = retriever.invoke(question)

    context = "\n".join(
        [doc.page_content for doc in docs]
    )

    prompt = f"""
    Answer using only the given context.

    Context:
    {context}

    Question:
    {question}
    """

    response = llm.invoke(prompt)

    return response.content
