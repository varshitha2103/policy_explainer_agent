from fastapi import FastAPI, Request
from app.retriever import router as retriever_router, startup as retriever_startup, retrieve_chunks
from app.simplifier import simplify_text
from app.examples import generate_examples

app = FastAPI()
app.include_router(retriever_router)

@app.on_event("startup")
def load_embeddings():
    retriever_startup()

@app.post("/explain_policy")
async def explain_policy(request: Request):
    data = await request.json()
    query = data.get("query")

    # Step 1: Retrieve
    top_chunks = retrieve_chunks(query)
    context = "\n".join(top_chunks["chunks"])

    # Step 2: Simplify
    simplified = simplify_text({"text": context})["simplified"]

    # Step 3: Examples
    examples = generate_examples({"text": context})["examples"]

    return {
        "query": query,
        "simplified": simplified,
        "examples": examples
    }
