import os

all_chunks = []

chunk_folder = "data/chunks"

for file in os.listdir(chunk_folder):

    path = os.path.join(chunk_folder, file)

    with open(path, "r", encoding="utf-8") as f:
        text = f.read()

    chunks = text.split("===== CHUNK")

    for chunk in chunks:

        chunk = chunk.strip()

        if len(chunk) > 50:
            all_chunks.append(chunk)

print("Total Chunks:", len(all_chunks))

from embedder import generate_embeddings

print("\nGenerating embeddings...")

embeddings = generate_embeddings(
    all_chunks
)

print(
    "Embedding Shape:",
    embeddings.shape
)
from vector_store import create_faiss_index

# ---------------------------------
# CREATE FAISS INDEX
# ---------------------------------

print("\nCreating FAISS index...")

index = create_faiss_index(
    embeddings
)

print(
    "Vectors Stored:",
    index.ntotal
)

from vector_store import search_index

# ---------------------------------
# ASK QUESTION
# ---------------------------------

query = input("\nAsk a question: ")

query_embedding = generate_embeddings(
    [query]
)[0]

distances, indices = search_index(
    index,
    query_embedding,
    k=3
)

print("\nTop Results:\n")

for idx in indices[0]:

    print("=" * 80)

    print(
        all_chunks[idx][:1000]
    )

    print("\n")