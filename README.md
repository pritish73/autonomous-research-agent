# 🧠 Autonomous Research Agent

An AI-powered Research Assistant that can read, understand, retrieve, and answer questions from research papers using Retrieval-Augmented Generation (RAG), FAISS vector search, and a local Llama 3 Large Language Model.

Instead of keyword matching, the system performs semantic search over research papers, retrieves the most relevant information, and generates context-aware answers with citations.

---

# 🚀 Features

✅ Read multiple research papers automatically

✅ Automatic text chunking

✅ Semantic search using Sentence Transformers

✅ FAISS Vector Database

✅ Cached embeddings for faster startup

✅ Cached FAISS index

✅ Local Llama 3 inference using Ollama

✅ Conversational memory

✅ Follow-up question understanding

✅ Context-aware retrieval

✅ Intelligent prompt routing

✅ Literature review generation

✅ Research gap identification

✅ Paper comparison

✅ Research paper summarization

✅ Source attribution

---

# 🏗️ System Architecture

```
                  Research Papers (PDF/TXT)
                           │
                           ▼
                  Text Extraction
                           │
                           ▼
                     Chunking Engine
                           │
                           ▼
               SentenceTransformer
                     Embeddings
                           │
                           ▼
                   FAISS Vector DB
                           │
                           ▼
                    User Question
                           │
                           ▼
                 Intent Detection
                           │
                           ▼
              Conversation Manager
                           │
             ┌─────────────┴─────────────┐
             │                           │
      New Question                Follow-up Question
             │                           │
             ▼                           ▼
      FAISS Retrieval          Previous Context
             │                           │
             └─────────────┬─────────────┘
                           ▼
                  Prompt Construction
                           │
                           ▼
                 Ollama (Llama 3)
                           │
                           ▼
                     Final Answer
```

---

# 📂 Project Structure

```
Autonomous-Research-Agent/
│
├── data/
│   ├── papers/
│   ├── chunks/
│   ├── embeddings.npy
│   └── faiss.index
│
├── embedder.py
├── vector_store.py
├── conversation_manager.py
├── intent_router.py
├── prompts.py
├── research_agent.py
│
├── requirements.txt
└── README.md
```

---

# 🧠 Supported Query Types

### General Question Answering

```
What is ReAct?
```

---

### Literature Review

```
Generate a literature review on AI Agents
```

---

### Comparison

```
Compare ReAct with Toolformer
```

---

### Research Gap Analysis

```
Find research gaps in Retrieval-Augmented Generation
```

---

### Summarization

```
Summarize the ReAct paper
```

---

### Follow-up Questions

```
What is ReAct?

↓

Summarize it.

↓

Compare it with Toolformer.

↓

Which one is better?
```

The assistant automatically remembers previous context and resolves follow-up questions without requiring another retrieval step.

---

# ⚙️ Technologies Used

- Python
- Sentence Transformers
- FAISS
- Ollama
- Llama 3
- NumPy
- Regular Expressions
- Retrieval-Augmented Generation (RAG)

---

# 🔥 Core Components

### Embedding Engine

- SentenceTransformer embeddings
- Embedding caching
- Fast semantic search

---

### Vector Database

- FAISS indexing
- Persistent vector storage
- Fast nearest-neighbor retrieval

---

### Intent Router

Automatically detects user intent:

- Question Answering
- Literature Review
- Comparison
- Summary
- Research Gap Analysis

---

### Conversation Manager

Maintains conversational context by:

- Tracking discussion topics
- Resolving follow-up questions
- Reusing previous retrieval results
- Avoiding unnecessary FAISS searches

---

### Prompt Router

Uses specialized prompts for different research tasks instead of relying on a single generic prompt.

---

# 📈 Current Capabilities

- Multiple research paper support
- Context-aware semantic retrieval
- Local LLM inference
- Automatic embedding caching
- Automatic FAISS index caching
- Context reuse for follow-up questions
- Research paper comparison
- Literature review generation
- Research gap detection
- Intelligent prompt selection

---

# 🚀 Future Improvements

- Upload PDFs while the assistant is running
- Automatic indexing of new papers
- Automatic topic extraction from retrieved papers
- Citation highlighting
- Web interface (Streamlit/FastAPI)
- Research paper recommendations
- Multi-document synthesis
- Export answers as PDF/DOCX

---

# 📷 Example

```
User:
What is ReAct?

Assistant:
ReAct is a reasoning and acting framework that combines language model reasoning with task execution...

Sources:
2210.03629v3.txt

--------------------------------------------

User:
Summarize it.

Assistant:
(Reuses previous context automatically)

--------------------------------------------

User:
Compare it with Toolformer.

Assistant:
(Automatically understands "it" refers to ReAct)
```

---

# 👨‍💻 Author

**Pritish Dutta**

AI • Machine Learning • Computer Vision • Large Language Models • Retrieval-Augmented Generation
