# 🧠 LegalMind AI

> AI-powered Legal Document Assistant using **Retrieval-Augmented Generation (RAG)**

<p align="center">

[![Live Demo](https://img.shields.io/badge/🚀%20Live%20Demo-Vercel-success?style=for-the-badge)](https://legalmind-ai-delta.vercel.app/)
[![Backend](https://img.shields.io/badge/⚡%20Backend-Railway-blue?style=for-the-badge)](https://legalmind-ai-production.up.railway.app/)
[![API Docs](https://img.shields.io/badge/📖%20Swagger-API%20Docs-green?style=for-the-badge)](https://legalmind-ai-production.up.railway.app/docs)

</p>

LegalMind AI is a full-stack AI-powered document assistant that enables users to upload PDF documents and ask natural language questions. The application uses **Retrieval-Augmented Generation (RAG)** with **ChromaDB**, **Sentence Transformers**, and **Google Gemini** to generate context-aware answers with source citations.

---

# 🌐 Live Demo

### 🚀 Frontend

https://legalmind-ai-delta.vercel.app/

### ⚡ Backend API

https://legalmind-ai-production.up.railway.app/

### 📖 Swagger API Documentation

https://legalmind-ai-production.up.railway.app/docs

---

## ✨ Features

- 📄 Upload PDF documents
- 🔍 Extract and chunk document text
- 🧠 Semantic search using Sentence Transformers
- 🗂️ Vector database using ChromaDB
- 🤖 AI-powered answers using Google Gemini
- 📚 Retrieval-Augmented Generation (RAG)
- 💬 Markdown formatted AI responses
- 📑 Source citations for every answer
- 🕒 Persistent chat history using SQLite
- 🗑️ Clear chat history
- 🌍 Live deployed application (Vercel + Railway)
- ⚡ FastAPI backend
- ⚛️ React frontend
- 📖 Interactive Swagger API documentation

---

# 🏗️ Architecture

```
                +----------------------+
                |     React Frontend   |
                +----------+-----------+
                           |
                    REST API Requests
                           |
                           ▼
                +----------------------+
                |    FastAPI Backend   |
                +----------+-----------+
                           |
          +----------------+----------------+
          |                                 |
          ▼                                 ▼
  PDF Processing                    SQLite Database
(PyMuPDF + Chunking)               Chat History
          |
          ▼
Sentence Transformers
      Embeddings
          |
          ▼
      ChromaDB
(Vector Database)
          |
          ▼
Retrieve Relevant Chunks
          |
          ▼
 Google Gemini API
          |
          ▼
 AI Generated Answer
```

---

# 🚀 Tech Stack

## Frontend

- React
- Vite
- Axios
- React Markdown
- CSS3

## Backend

- FastAPI
- Uvicorn
- Python
- Google Gemini API
- Sentence Transformers
- ChromaDB
- SQLite
- PyMuPDF

---

# 📂 Project Structure

```
legalmind-ai/

├── backend/
│   ├── app/
│   │   ├── api/
│   │   ├── core/
│   │   ├── database/
│   │   ├── rag/
│   │   ├── schemas/
│   │   ├── services/
│   │   └── main.py
│   │
│   ├── vector_db/
│   ├── uploads/
│   ├── requirements.txt
│   └── .env
│
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   ├── services/
│   │   ├── styles/
│   │   └── App.jsx
│   │
│   ├── package.json
│   └── vite.config.js
│
├── README.md
└── .gitignore
```

---

# ⚙️ Installation

## Clone Repository

```bash
git clone https://github.com/nandinii-259/legalmind-ai.git

cd legalmind-ai
```

---

# Backend Setup

```bash
cd backend

python -m venv venv
```

Activate virtual environment

### Windows

```bash
venv\Scripts\activate
```

### macOS/Linux

```bash
source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Create `.env`

```env
GEMINI_API_KEY=YOUR_API_KEY

MODEL_NAME=gemini-2.5-flash

DATABASE_URL=sqlite:///legalmind.db

CHROMA_PATH=vector_db
```

Run backend

```bash
uvicorn app.main:app --reload --port 8001
```

Backend runs at

```
http://localhost:8001
```

Swagger

```
http://localhost:8001/docs
```

---

# Frontend Setup

```bash
cd frontend

npm install
```

Create `.env`

```env
VITE_API_URL=http://localhost:8001
```

Run frontend

```bash
npm run dev
```

Frontend runs at

```
http://localhost:5173
```

---

# 🚀 Deployment

| Service | Platform |
|----------|----------|
| Frontend | Vercel |
| Backend | Railway |
| AI Model | Google Gemini |
| Vector Database | ChromaDB |
| Database | SQLite |

---

# API Endpoints

| Method | Endpoint | Description |
|---------|----------|-------------|
| POST | `/upload/` | Upload PDF |
| POST | `/chat/` | Ask AI Questions |
| GET | `/history/` | Retrieve Chat History |
| DELETE | `/history/` | Clear Chat History |

---

# AI Pipeline

```
Upload PDF
      │
      ▼
Extract Text
      │
      ▼
Chunk Document
      │
      ▼
Generate Embeddings
      │
      ▼
Store in ChromaDB
      │
      ▼
User asks Question
      │
      ▼
Semantic Retrieval
      │
      ▼
Relevant Chunks
      │
      ▼
Google Gemini
      │
      ▼
Final Answer + Sources
```

---

# 🚀 Future Improvements

- User Authentication
- Multi-document support
- Streaming AI responses
- Drag & Drop upload
- Dark Mode
- Docker Support
- AWS Deployment
- Role-based Access Control
- Conversation Memory
- Multiple LLM Support

---

# 📚 Learning Outcomes

This project helped in learning:

- Retrieval-Augmented Generation (RAG)
- FastAPI Development
- React Development
- REST API Development
- Google Gemini API
- Sentence Transformers
- ChromaDB
- Vector Search
- Semantic Search
- Prompt Engineering
- SQLite
- Full Stack AI Development
- Git & GitHub
- Railway Deployment
- Vercel Deployment

---

# 👩‍💻 Author

## Nandini Agrawal

Electronics & Telecommunication Engineering Student

AI Engineer • Full Stack Developer • Software Engineering Enthusiast

If you found this project useful, consider giving it a ⭐ on GitHub!

---

# 📄 License

This project is licensed under the **MIT License**.