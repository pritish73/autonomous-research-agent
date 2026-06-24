from embedder import generate_embeddings
from vector_store import create_faiss_index

chunks = [
    "Attention is all you need",
    "Retrieval augmented generation",
    "Transformers use self attention",
    "Large language models"
]

embeddings = generate_embeddings(
    chunks
)

index = create_faiss_index(
    embeddings
)

print(
    "Total vectors:",
    index.ntotal
)