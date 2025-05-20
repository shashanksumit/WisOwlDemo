from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

class BERTMatcher:
    def __init__(self, text1, text2):
        self.text1 = text1
        self.text2 = text2
        self.model = SentenceTransformer('all-MiniLM-L6-v2')  # small, fast & accurate

    def compute_similarity(self):
        embeddings = self.model.encode([self.text1, self.text2])
        score = cosine_similarity([embeddings[0]], [embeddings[1]])[0][0] * 100
        return round(score, 2)