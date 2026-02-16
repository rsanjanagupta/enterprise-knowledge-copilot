from sentence_transformers import SentenceTransformer

# Load SAME model used during indexing
model = SentenceTransformer("all-MiniLM-L6-v2")

def embed_query(query: str):
    """
    Converts user question into embedding vector
    """
    embedding = model.encode([query])
    return embedding
