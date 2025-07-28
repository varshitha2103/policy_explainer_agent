from fastapi import APIRouter
from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

router = APIRouter()

chunks = []
model = SentenceTransformer('all-MiniLM-L6-v2')
index = None

@router.on_event("startup")
def startup():
    global chunks, index
    reader = PdfReader("data/healthcare_policy.pdf")
    text = "\n".join([page.extract_text() for page in reader.pages if page.extract_text()])
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    chunks = splitter.split_text(text)
    
    embeddings = model.encode(chunks)
    index = faiss.IndexFlatL2(embeddings.shape[1])
    index.add(np.array(embeddings))

@router.get("/retrieve_chunks")
def retrieve_chunks(query: str, k: int = 3):
    query_vec = model.encode([query])
    _, indices = index.search(query_vec, k)
    return {"chunks": [chunks[i] for i in indices[0]]}
