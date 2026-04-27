from fastapi import FastAPI
from processing.pdf_loader import load_pdf
from processing.chunker import chunk_text
from embedding.model import get_embeddings
from search.vector_store import add_embeddings, search
from embedding.llm import generate_answer
import uvicorn
from connectors.google_drive import fetch_files, download_file
from fastapi.responses import RedirectResponse

app = FastAPI()

@app.get("/")
def home():
    return RedirectResponse(url="/docs")

@app.get("/load")
def load_data():
    text = load_pdf("AI_Platform_Engineer_RAG_Assignment.pdf")
    chunks = chunk_text(text)

    print("Chunks created:", len(chunks))

    embeddings = get_embeddings(chunks)
    add_embeddings(embeddings, chunks)

    return {"message": "Data loaded successfully"}


@app.get("/ask")
def ask(query: str):
    query_embedding = get_embeddings([query])[0]
    results = search(query_embedding)

    if not results:
        return {"answer": "No data found. Please load documents first.", "sources": []}

    context = "\n".join([r["text"] for r in results])
    sources = list(set([r["source"] for r in results]))

    answer = generate_answer(query, context)

    return {
        "answer": answer,
        "sources": sources
    }

@app.post("/sync-drive")
def sync_drive():
    files = fetch_files()

    for f in files:
        if f["name"].endswith(".pdf"):
            content = download_file(f["id"])

            # Save file temporarily
            with open(f["name"], "wb") as temp_file:
                temp_file.write(content)

            # Process same as /load
            text = load_pdf(f["name"])
            chunks = chunk_text(text)

            embeddings = get_embeddings(chunks)
            add_embeddings(embeddings, chunks)

    return {"message": "Drive synced and data loaded"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8001)