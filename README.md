# 🧾 Policy Explainer Agent

A locally running, agentic RAG-powered AI app that **explains complex healthcare policies in simple language with examples** — all without sending data to external APIs.

> 🔧 Built with FastAPI + Streamlit + Ollama + Local LLM

---

## 🚀 Overview

This project lets users upload healthcare policy PDFs and returns:
- 🧠 A **simple, understandable explanation** (5th-grade level)
- 💡 Two real-world examples for better clarity
- 🔍 Transparent, agentic flow with step-by-step processing

---

## 🧠 Architecture

```mermaid ```
graph LR
A[PDF Upload] --> B[Retriever Agent (RAG)]
B --> C[Simplifier Agent (LLM)]
C --> D[Example Generator Agent]
D --> E[Final Response]

🔄 Agentic Flow:
Retriever: Extracts relevant content from uploaded PDF
Simplifier: Converts into simplified text
Example Generator: Generates 2 real-world examples
MCP Coordination: Manages all agent interactions

🛠 Tech Stack
Tool	Purpose
FastAPI	Backend and MCP API Server
Streamlit	User Interface
Ollama	Run local LLM (e.g., Mistral)
PyPDF2	Extract text from PDFs
LangChain	Modular agent orchestration

📁 Project Structure

policy-explainer-agent/
├── app/
│   ├── main.py               # FastAPI backend entrypoint
│   ├── agents.py             # Agent definitions (Retriever, Simplifier, Examples)
│   ├── retriever.py          # PDF extraction and preprocessing
│   └── utils.py              # Helper functions
├── ui_app.py                 # Streamlit UI
├── test_request.py           # Optional testing script
├── requirements.txt
├── README.md

🔧 Setup Instructions
1. Clone the Repo
```bash
git clone https://github.com/your-username/policy-explainer-agent.git
cd policy-explainer-agent
```
2. Install Dependencies
```bash
pip install -r requirements.txt
```
3. Run Ollama with Mistral
Make sure Ollama is installed and Mistral is downloaded:
```bash
ollama run mistral
```
If not installed:
```bash
ollama pull mistral
```
4. Start the FastAPI Backend
```bash
uvicorn app.main:app --reload
```
5. Launch the Streamlit UI
```bash
streamlit run ui_app.py
```

💻 Example Use Case
User Uploads: healthcare_policy.pdf
System Responds:
📝 Plain-language summary
💡 2 relatable examples (e.g., for patients, providers)
✅ Agent trace (RAG → Simplifier → Example builder)

🌐 Deployment (Optional)
Deploy to Streamlit Cloud:
Push repo to GitHub
Go to https://streamlit.io/cloud
Link your GitHub & select this repo
Set ui_app.py as the entrypoint


