"""
Developer Name: Sai Sundeep Rayidi
Creation Date: 11/20/2024
Last Update Date: 11/30/2024

"""


import numpy as np
from sentence_transformers import SentenceTransformer

model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')


def vectorize_text(text_data):
    return model.encode(text_data)


def save_embeddings(embeddings, path):
    # Save embeddings to file
    np.save(path, embeddings)
