import os
import numpy as np
import pandas as pd
import json
from utils.data_loader import load_data
from utils.preprocessing import preprocess_job_descriptions
from utils.vectorization import vectorize_text, save_embeddings
from utils.similarity import find_top_k_similar_jobs
from utils.model import train_knn_model, load_knn_model
from resume_parser import process_resume


def main(resume_path):
    # Check if a pre-trained model exists
    model_path = "models/job_desc_cluster.joblib"
    embeddings_path = "models/job_description_embeddings.npy"
    pre_processed_data_path = "data/preprocessed_data.csv"
    processed_job_descriptions = pd.read_csv(pre_processed_data_path)

    if os.path.exists(model_path) and os.path.exists(embeddings_path):
        # If model and embeddings exist, load them
        knn_model = load_knn_model(model_path)
        job_desc_embeddings = np.load(embeddings_path)
    else:
        # Load and preprocess the data, then vectorize
        job_data = load_data()
        cleaned_job_desc = preprocess_job_descriptions(job_data["Job Description"])
        job_desc_embeddings = vectorize_text(job_data["Job Description"].values)

        # Save embeddings to avoid reprocessing
        save_embeddings(job_desc_embeddings, embeddings_path)

        # Train and save KNN model
        knn_model = train_knn_model(job_desc_embeddings)
        knn_model.save(model_path)

    # Parse resume and vectorize it
    resume_text = process_resume(resume_path)
    resume_embedding = vectorize_text([resume_text])

    # Find top K similar job descriptions
    top_jobs = find_top_k_similar_jobs(knn_model, resume_embedding, job_desc_embeddings)

    # Create a list to store the results in the desired JSON format
    job_results = []
    for idx, score in top_jobs:
        job = {
            "job_title": processed_job_descriptions.iloc[idx]["Job Title"],
            "job_description": processed_job_descriptions.iloc[idx]["Job Description"],
            "matching_score": float(round(score, 4))  # Round the score to 4 decimal places for clarity
        }
        job_results.append(job)

    # Convert the list to a JSON object
    job_results_json = json.dumps(job_results, indent=4)
    return job_results_json


if __name__ == "__main__":
    resume_path = "software_engineer_resume.pdf"
    results_json = main(resume_path)
    print(results_json)
