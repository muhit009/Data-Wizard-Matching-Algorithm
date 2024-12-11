"""
Developer Name: Sai Sundeep Rayidi
Creation Date: 11/20/2024
Last Update Date: 11/30/2024

"""


from sklearn.metrics.pairwise import cosine_similarity


def find_top_k_similar_jobs(knn_model, resume_embedding, job_desc_embeddings, top_k=5):
    distances, indices = knn_model.kneighbors(resume_embedding)
    job_desc_embeddings_selected = job_desc_embeddings[indices[0]]  # Get the job descriptions for top K matches
    cosine_similarities = cosine_similarity(resume_embedding, job_desc_embeddings_selected).flatten()
    top_jobs = [(idx, similarity) for idx, similarity in zip(indices[0], cosine_similarities)]

    return top_jobs[:top_k]
