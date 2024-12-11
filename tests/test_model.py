import unittest
from matching_algorithm.utils.model import train_knn_model, load_knn_model
import numpy as np
from unittest.mock import patch, MagicMock

class TestModel(unittest.TestCase):

    @patch('joblib.load')
    def test_load_knn_model(self, mock_load):
        # Mock the joblib.load function
        mock_knn = MagicMock()
        mock_load.return_value = mock_knn

        knn_model = load_knn_model('models/job_desc_cluster.joblib')

        # Check that the model is loaded correctly
        self.assertEqual(knn_model, mock_knn)

    def test_train_knn_model(self):
        embeddings = np.array([[0.1, 0.2], [0.3, 0.4]])
        knn_model = train_knn_model(embeddings)

        # Check if the trained model is a NearestNeighbors instance
        from sklearn.neighbors import NearestNeighbors
        self.assertIsInstance(knn_model, NearestNeighbors)

if __name__ == '__main__':
    unittest.main()
