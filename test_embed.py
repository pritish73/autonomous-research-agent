# DAY 3: EMBEDDING ENGINE
#
# Goal:
# Convert text chunks into numerical vectors.
#
# Example:
#
# "Attention is all you need"
#
# becomes
#
# [0.0122, -0.0139, 0.0342, ...]
#
# Why?
#
# Computers cannot understand raw text.
# They can compare vectors mathematically.
#
# Similar meanings -> Similar vectors
#
# Example:
#
# "Transformer architecture"
# "Self-attention model"
#
# produce embeddings that are close together.
#
# This enables:
#
# Semantic Search
# Retrieval-Augmented Generation (RAG)
# Research Paper QA
# Paper Comparison
# Research Gap Detection
#
# Next Step:
#
# Embeddings -> FAISS Vector Database

from embedder import generate_embeddings

chunks = [
    "Attention is all you need",
    "Retrieval Augmented Generation"
]

embeddings = generate_embeddings(chunks)

print("Shape:", embeddings.shape)

print("\nFirst Embedding:\n")
print(embeddings[0][:10])