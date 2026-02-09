from langchain_community.document_loaders import PyPDFLoader

def load_documents(path):
    loader = PyPDFLoader(path)
    return loader.load()

if __name__ == "__main__":
    docs = load_documents("data/docs/DReam-VL.pdf")
    print(f"Loaded {len(docs)} pages")
