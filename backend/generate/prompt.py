def build_prompt(context_chunks, question):
    context_text = ""

    for i, chunk in enumerate(context_chunks):
        context_text += f"\n[Source {i+1}]\n{chunk.page_content}\n"

    prompt = f"""
You are an enterprise knowledge assistant.
You MUST answer only from the context below.
If the answer is not present, say:
"I don't know based on the provided documents."

Context:
{context_text}

Question:
{question}

Answer:
"""

    return prompt
