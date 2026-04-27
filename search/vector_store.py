import faiss
import numpy as np

dimension = 384
index = faiss.IndexFlatL2(dimension)

stored_data = []   # ✅ changed

def add_embeddings(embeddings, chunks):
    global stored_data
    
    for emb, chunk in zip(embeddings, chunks):
        index.add(np.array([emb]))
        
        stored_data.append({
            "text": chunk,
            "source": "AI_Platform_Engineer_RAG_Assignment.pdf"  # or sample.pdf
        })


def search(query_embedding, k=3):
    distances, indices = index.search(np.array([query_embedding]), k)

    results = []

    for i in indices[0]:
        if i >= 0 and i < len(stored_data):
            results.append(stored_data[i])

    return results