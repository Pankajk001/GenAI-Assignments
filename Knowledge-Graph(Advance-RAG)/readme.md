# 🧠 Memory-Aware Conversational AI

This project demonstrates a sophisticated, memory-enhanced chatbot built with Python. It leverages the `mem0` library to create a **stateful agent** that learns from interactions and maintains **long-term memory**. The agent combines a **vector database** for semantic search and a **graph database** for storing structured knowledge, all orchestrated to provide context-aware responses using an advanced **Large Language Model (LLM)**.

---

## 🚀 Core Technologies

This application is built on a modern stack for **Retrieval-Augmented Generation (RAG)**:

- **🧠 Orchestration: [`mem0`](https://github.com/mem0ai/mem0)**  
It's a light weight library which internally by using Graph-database and vector-DB acts as a memory. Simplifies the creation of memory-aware AI systems by managing memory types and backend services.

- **🧠 LLM & Embeddings: [OpenAI](https://openai.com)**  
  Uses:
  - `gpt-4.1` for intelligent response generation  
  - `text-embedding-3-small` for vector embeddings

- **🗂️ Vector Store: [Qdrant](https://qdrant.tech)**  
  A high-performance vector database for storing and searching text embeddings.

- **🧩 Graph Store: [Neo4j](https://neo4j.com)**  
  A graph database for storing structured knowledge extracted from conversations.

---

## 🔁 How It Works

The system follows a continuous loop for each user message:

1. **Retrieve**  
   - Converts user input into a vector and searches similar memories in Qdrant.
   - Optionally queries Neo4j for related entities.

2. **Augment**  
   - Injects the retrieved memories into the system prompt given to the LLM.

3. **Generate**  
   - GPT-4.1 generates a context-aware response based on memory + user query.

4. **Update**  
   - The message and response are saved into memory.
   - Embeddings are created and stored in Qdrant and Neo4j for future reference.

---

