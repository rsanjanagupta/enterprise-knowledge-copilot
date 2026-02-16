from pipeline.qa_pipeline import answer_question

if __name__ == "__main__":
    question = input("Enter your question: ")

    answer, sources = answer_question(question)

    print("\nAnswer:\n", answer)
    print("\nSources:")
    for src in sources:
        source = src.metadata.get("source", "Unknown")
        page = src.metadata.get("page", "N/A")
        print(f"- {source} (page {page})")

