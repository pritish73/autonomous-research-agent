from embedder import generate_embeddings

from vector_store import (
    create_faiss_index,
    search_index
)

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

query = "How does self attention work?"

query_embedding = generate_embeddings(
    [query]
)[0]

distances, indices = search_index(
    index,
    query_embedding
)

print("\nTop Results:\n")

for idx in indices[0]:

    print(chunks[idx])