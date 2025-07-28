from fastapi import APIRouter
import ollama

router = APIRouter()

@router.post("/generate_examples")
def generate_examples(payload: dict):
    text = payload["text"]
    messages = [
        {"role": "system", "content": "You are an assistant that creates easy-to-understand real-life examples about healthcare policies."},
        {"role": "user", "content": f"Give 2 real-life examples that explain this policy:\n\n{text}"}
    ]
    response = ollama.chat(model="mistral", messages=messages)
    return {"examples": response["message"]["content"]}
