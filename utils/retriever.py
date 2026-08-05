from vector_db.chroma_store import load_vector_store

def retrieve_documents(question):
    db = load_vector_store()

    retriever = db.as_retriever(
        search_kwargs={"k":3}
    )

    docs = retriever.invoke(question)

    return docs
