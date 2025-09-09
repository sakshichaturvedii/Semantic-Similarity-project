# Task Report

## Part A – Semantic Similarity Model

**Objective:**  
Build an algorithm to quantify semantic similarity between two text paragraphs. Output should be a score between **0 (dissimilar)** and **1 (highly similar)**.

**Approach:**  
- Used a **pre-trained SentenceTransformer model** (`all-MiniLM-L6-v2`) to generate embeddings for each text.  
- Calculated **cosine similarity** between embeddings.  
- Normalized the cosine similarity from [-1, 1] to [0, 1] using:  

similarity = (cosine_similarity + 1) / 2


- This provides a **semantic similarity score** that captures meaning, not just keyword overlap.  

**Outcome:**  
- Score **1 → highly similar**, **0 → highly dissimilar**  
- Works without labeled data as the model is pre-trained on large semantic similarity tasks.

---

## Part B – API Deployment

**Objective:**  
Expose the semantic similarity model as a REST API endpoint for real-time requests.

**Implementation:**  
- **Flask** API with POST endpoint `/similarity`.  
- **Request body:**  
```json
{ "text1": "sample text one", "text2": "sample text two" }
```

- **Response body:**
```json 
{ "similarity score": 0.6}
```

**Deployment:**

- Dockerfile included to enable containerization for portability if needed.
