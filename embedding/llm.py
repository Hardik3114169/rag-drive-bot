from transformers import pipeline

qa_pipeline = pipeline("text-generation", model="gpt2")

def generate_answer(query, context):
    prompt = f"""
You are an AI assistant.

Answer the question based ONLY on the context below.
If the answer is not in the context, say: "Not found in documents".

Give answer in 2-3 clear lines.

Context:
{context}

Question:
{query}

Answer:
"""

    result = qa_pipeline(prompt, max_length=200, do_sample=True)[0]["generated_text"]

    # Extract only answer part
    return result.split("Answer:")[-1].strip()