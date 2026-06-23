# Autonomous Research Agent

An AI-powered research assistant that automates the process of reading, processing, and understanding research papers. The system converts academic documents into searchable semantic representations, forming the foundation for semantic search, Retrieval-Augmented Generation (RAG), literature review generation, and research gap detection.

## Features

- Extract text from PDF research papers
- Process multiple papers automatically
- Split papers into semantic chunks
- Generate vector embeddings using transformer models
- Prepare documents for semantic search and RAG workflows
- Scalable architecture for future multi-agent research systems



## Technologies Used

- Python
- PyMuPDF
- Sentence Transformers
- PyTorch
- FAISS
- Hugging Face Transformers

## Project Architecture

```text
Research Papers (PDFs)
           ↓
      Text Extraction
           ↓
      Text Chunking
           ↓
   Embedding Generation
           ↓
      Vector Database
           ↓
      Semantic Search
           ↓
        LLM Layer
           ↓
      Research Agent
```

## Current Capabilities

### PDF Processing
- Read research papers from a local directory
- Extract raw text from PDF documents

### Chunking Engine
- Split large research papers into manageable chunks
- Preserve contextual continuity using overlapping chunks

### Embedding Engine
- Convert text chunks into dense vector representations
- Enable semantic understanding and similarity search

## Project Structure

```text
Autonomous Research Agent/
│
├── papers/
├── data/
│   ├── chunks/
│   └── embeddings/
│
├── pdf_reader.py
├── chunker.py
├── embedder.py
├── main.py
├── README.md
└── .gitignore
```

## Future Enhancements

- FAISS Vector Database Integration
- Semantic Search Engine
- Research Paper Question Answering
- Multi-Paper Comparison
- Literature Review Generation
- Research Gap Detection
- Multi-Agent Research Workflows
- Autonomous Research Report Generation

## Author

Pritish Dutta
