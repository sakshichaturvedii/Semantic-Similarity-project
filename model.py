from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer("all-MiniLM-L6-v2")

def similarity_score(text1: str, text2: str) -> float:
    """
    Compute semantic similarity between two texts.
    Returns a score between 0 (dissimilar) and 1 (similar).
    """
    emb1 = model.encode(text1, convert_to_numpy=True)
    emb2 = model.encode(text2, convert_to_numpy=True)
    cos_sim = util.cos_sim(emb1, emb2).item()
    return (cos_sim + 1) / 2   