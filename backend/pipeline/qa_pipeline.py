from retrieve.search import search_similar_chunks
from generate.prompt import build_prompt
from generate.answer import generate_answer

def answer_question(question: str):
    chunks = search_similar_chunks(question, top_k=3)

    if not chunks:
        return "I don't know based on the provided documents.", []

    prompt = build_prompt(chunks, question)
    answer = generate_answer(prompt)

    return answer, chunks
