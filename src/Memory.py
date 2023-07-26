# Memory.py
# Memory.py

from collections import deque
from sentence_transformers import SentenceTransformer
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

class Memory:
    def __init__(self):
        # Initialize an empty memory
        self.records = []

    def __init__(self, max_size=1000):
        # Initialize an empty memory
        self.records = deque(maxlen=max_size)
        self.embedding_model = SentenceTransformer('all-MiniLM-L6-v2')

    def remember(self, interaction):
        # Store the interaction in memory
        self.records.append(interaction)

    def recall(self, context, top_k=1):
        # Retrieve relevant memory given a context
        # Convert context and records to embeddings
        context_embedding = self.embedding_model.encode([context])
        record_embeddings = self.embedding_model.encode([record.prompt for record in self.records])
        # Compute cosine similarity
        similarities = cosine_similarity(context_embedding, record_embeddings)
        # Get top k indices
        top_indices = np.argsort(similarities, axis=-1)[:, -top_k:]
        # Return top k records
        return [self.records[index] for index in top_indices[0]]

    def get_last_n(self, n):
        # Get the last n interactions from memory
        return list(self.records)[-n:]
