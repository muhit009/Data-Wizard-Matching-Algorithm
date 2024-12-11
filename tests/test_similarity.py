import unittest
from matching_algorithm.utils.similarity import find_top_k_similar_jobs
from unittest.mock import MagicMock
import numpy as np

class TestSimilarity(unittest.TestCase):

    def test_find_top_k_similar_jobs(self):
        # Mock KNN model and job descriptions
        knn_model = MagicMock()
        knn_model.kneighbors.return_value = (np.array([[0, 1]]), np.array([[0.9, 0.8]]))  # Mock nearest neighbors
        resume_embedding = np.array([[0.5, 0.5]])  # Mock resume embedding
        job_desc_embeddings = np.array([[0.9, 0.1], [0.4, 0.4]])  # Mock job descriptions

        top_jobs = find_top_k_similar_jobs(knn_model, resume_embedding, job_desc_embeddings, top_k=2)

        # Check that the top jobs returned match the expected output
        self.assertEqual(len(top_jobs), 2)
        self.assertEqual(top_jobs[0][0], 0)  # Check first job index
        self.assertGreater(top_jobs[0][1], 0.8)  # Check similarity score is as expected

if __name__ == '__main__':
    unittest.main()
