# 🧠 LegalMind AI

> AI-powered Legal Document Assistant using **Retrieval-Augmented Generation (RAG)**

LegalMind AI is a full-stack AI application that allows users to upload PDF documents and ask natural language questions. The system retrieves relevant document chunks using vector search and generates context-aware answers using Google's Gemini model.

---

## ✨ Features

- 📄 Upload PDF documents
- 🔍 Extract and chunk document text
- 🧠 Semantic search using Sentence Transformers
- 🗂️ Vector database with ChromaDB
- 🤖 AI-powered answers using Google Gemini
- 📚 Retrieval-Augmented Generation (RAG)
- 💬 Markdown formatted AI responses
- 📑 Source citations for every answer
- 🕒 Persistent chat history using SQLite
- 🗑️ Clear chat history
- ⚡ FastAPI backend
- ⚛️ React frontend
- 📖 Interactive Swagger API documentation

---

## 🏗️ Architecture

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
- Google Gemini API
- Sentence Transformers
- ChromaDB
- SQLite
- PyMuPDF
- Python

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
│   ├── chroma_db/
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
git clone https://github.com/YOUR_USERNAME/legalmind-ai.git

cd legalmind-ai
```

---

# Backend Setup

```bash
cd backend

python -m venv venv

venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Create `.env`

```env
GEMINI_API_KEY=YOUR_API_KEY

MODEL_NAME=gemini-3.5-flash
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

Create

```
.env
```

```env
VITE_API_URL=http://localhost:8001
```

Run frontend

```bash
npm run dev
```

Frontend

```
http://localhost:5173
```

---

# API Endpoints

| Method | Endpoint | Description |
|---------|----------|-------------|
| POST | `/upload/` | Upload PDF |
| POST | `/chat/` | Ask Questions |
| GET | `/history/` | Get Chat History |
| DELETE | `/history/` | Clear Chat History |

---

# AI Pipeline

```
Upload PDF

↓

Extract Text

↓

Chunk Text

↓

Generate Embeddings

↓

Store in ChromaDB

↓

User asks Question

↓

Semantic Retrieval

↓

Relevant Chunks

↓

Gemini LLM

↓

Final Answer + Sources
```
---

# Future Improvements

- Authentication
- Multi-document support
- Streaming AI responses
- Drag & Drop upload
- Dark mode
- Docker support
- AWS Deployment
- Role-based access

---

# Learning Outcomes

This project helped in learning:

- Retrieval-Augmented Generation (RAG)
- FastAPI Development
- React Development
- REST APIs
- Vector Databases
- Embedding Models
- Prompt Engineering
- Google Gemini API
- ChromaDB
- SQLite
- Full Stack AI Development

---

# Author

**Nandini Agrawal**

Electronics & Telecommunication Engineering

AI & Software Engineering Enthusiast

---

# License

This project is licensed under the MIT License.
