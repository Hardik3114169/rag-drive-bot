# RAG-Based Document Q&A System with Google Drive Integration 
1. Overview 
This project is a Retrieval-Augmented Generation (RAG) system that connects to Google Drive, 
processes documents, and enables users to ask questions based on the content of those 
documents. 
The system fetches files from Google Drive, extracts and processes their content, converts them 
into embeddings, stores them in a vector database, and uses an LLM to generate answers 
grounded in the retrieved context. 
 
2. Objective 
The goal of this project is to: 
• Connect to Google Drive and fetch documents  
• Process and chunk document content  
• Generate embeddings for semantic understanding  
• Store embeddings using FAISS  
• Retrieve relevant content based on user queries  
• Generate answers using an LLM  
 
3.  System Architecture 
Google Drive / Local PDF 
        ↓ 
   Text Extraction 
        ↓ 
     Chunking 
        ↓ 
   Embeddings (Sentence Transformers) 
        ↓ 
   FAISS Vector Store 
        ↓ 
 User Query → Embedding 
        ↓ 
Similarity Search 
↓ 
Context Retrieval 
↓ 
LLM (Answer Generation) 
↓ 
Final Answer + Sources 
4. Features Implemented 
1. Google Drive Integration 
• Connected using Service Account  
• Fetches files via API  
• Supports PDF ingestion  
• Endpoint: POST /sync-drive  
2. Document Processing 
• Extracts text from PDFs  
• Splits text into manageable chunks  
• Prepares data for embedding  
3. Embedding Layer 
• Uses Sentence Transformers  
• Converts text into vector representations  
• Supports semantic similarity search  
4. Vector Storage (FAISS) 
• Stores embeddings along with text  
• Enables fast similarity-based retrieval  
• Used as a lightweight vector database  
5. Query System (RAG) 
• Endpoint: GET /ask  
• Converts query into embedding  
• Retrieves top relevant chunks  
• Passes context to LLM  
6. AI Answer Generation 
• Uses Hugging Face Transformer model  
• Generates answers based on retrieved context  
• Returns:  
o Answer  
o Source documents  
5. Tech Stack 
• Backend: Python, FastAPI  
• Embeddings: Sentence Transformers  
• Vector Database: FAISS  
• LLM: Hugging Face Transformers  
• Cloud Integration: Google Drive API  
6. API Endpoints 
a. Load Local PDF 
GET /load 
b. Sync Google Drive Files 
POST /sync-drive 
c. Ask Questions 
GET /ask?query=your_question 
7. Example Query 
What is this assignment about? 
Example Response: 
{ 
} 
"answer": "This assignment involves building a RAG-based system...", 
"sources": ["AI_Platform_Engineer_RAG_Assignment.pdf"] 
8. Key Concepts Used 
• Retrieval-Augmented Generation (RAG)  
• Embeddings & Semantic Search  
• Vector Databases (FAISS)  
• Prompt-based LLM Response Generation  
9. Limitations 
• Basic LLM (Hugging Face) → limited answer quality  
• No caching (reprocessing occurs)  
• No UI (API-based interaction only)  
10. Future Improvements 
• Use advanced LLM (OpenAI / Llama)  
• Add frontend UI (Chat interface)  
• Implement caching and incremental sync  
• Improve chunking strategy  
• Add metadata filtering  
11. Summary 
This project demonstrates the complete pipeline of a production-style RAG system, integrating: 
• Data ingestion  
• Vector search  
• AI-based answer generation  
• Cloud-based document retrieval  
