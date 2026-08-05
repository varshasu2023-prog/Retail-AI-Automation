def generate_answer(vector_db, question):

    docs = vector_db.similarity_search(
        question,
        k=3
    )

    answer = "\n\n".join(
        [doc.page_content for doc in docs]
    )

    return answer
