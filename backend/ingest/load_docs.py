import os
from langchain_community.document_loaders import PyPDFLoader

def load_documents(pdf_dir):
    documents = []

    print("DEBUG: pdf_dir =", pdf_dir)
    print("DEBUG: files in dir =", os.listdir(pdf_dir))

    for filename in os.listdir(pdf_dir):
        print("DEBUG: checking file:", filename)

        if filename.lower().endswith(".pdf"):
            file_path = os.path.join(pdf_dir, filename)
            print("DEBUG: loading PDF:", file_path)

            loader = PyPDFLoader(file_path)
            pages = loader.load()

            print(f"DEBUG: loaded {len(pages)} pages from {filename}")
            documents.extend(pages)

    print("DEBUG: total pages loaded =", len(documents))
    return documents