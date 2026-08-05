from vector_db.chroma_store import load_database

def retrieve(question):

    db = load_database()

    retriever = db.as_retriever(
        search_kwargs={"k":3}
    )

    docs = retriever.invoke(question)

    return docs
