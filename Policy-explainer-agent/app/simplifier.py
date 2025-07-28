from fastapi import APIRouter
import ollama

router = APIRouter()

@router.post("/simplify_text")
def simplify_text(payload: dict):
    text = payload["text"]
    messages = [
        {"role": "system", "content": "You are a helpful assistant who explains complex healthcare policies in simple, 5th-grade English."},
        {"role": "user", "content": f"Simplify the following:\n\n{text}"}
    ]
    response = ollama.chat(model="mistral", messages=messages)
    return {"simplified": response["message"]["content"]}
