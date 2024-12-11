"""
Developer Name: Sai Sundeep Rayidi
Creation Date: 11/20/2024
Last Update Date: 11/30/2024

"""

from sklearn.neighbors import NearestNeighbors
import joblib


def train_knn_model(job_desc_embeddings, n_neighbors=8):
    knn = NearestNeighbors(n_neighbors=n_neighbors, algorithm='ball_tree')
    knn.fit(job_desc_embeddings)

    return knn


def load_knn_model(model_path='models/job_desc_cluster.joblib'):
    # Load the pre-trained KNN model
    return joblib.load(model_path)
