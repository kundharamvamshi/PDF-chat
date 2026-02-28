# PDF-chat-Langchain-RAG-Gemini-
Chat with your pdf using RAG System and google Gemini 

# 📄 Gemini RAG PDF Chatbot (LangChain + Streamlit + Chroma)

A Retrieval-Augmented Generation (RAG) application that allows users to chat with their PDF documents using **Google Gemini**, **LangChain**, **ChromaDB**, and **Streamlit**.

---

## 🚀 Features

* 📂 Upload and process PDFs
* ✂️ Smart text chunking with LangChain
* 🧠 Google Gemini embeddings for semantic search
* 🗂️ Persistent vector database using Chroma
* 💬 Conversational question answering over your documents
* ⚡ Streamlit interactive UI

## 🏗️ Tech Stack

* **LLM:** Google Gemini (`gemini-2.5-flash`)
* **Framework:** LangChain
* **Vector Store:** ChromaDB
* **Frontend:** Streamlit
---

## 📁 Project Structure

```
├── app.py                 # Streamlit application
├── requirements.txt
├── chroma_db/            # Persistent vector store
├── data/                 # PDF documents
└── README.md
```

---

## ⚙️ Installation

### 1️⃣ Clone the repository

```bash
git clone https://github.com/kundharamvamshi/gemini-rag-pdf-chat.git
cd gemini-rag-pdf-chat
```

---

### 2️⃣ Create virtual environment

```bash
python -m venv venv
venv\Scripts\activate     

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Setup API Key

Create a `.env` file or set environment variable:

```env
GOOGLE_API_KEY=your_api_key_here
```

## ▶️ Run the App

```bash
streamlit run app.py
```
* Streamlit

