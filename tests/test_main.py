import unittest
from matching_algorithm.main import main
from unittest.mock import patch, MagicMock

class TestMain(unittest.TestCase):

    @patch('main.load_data')
    @patch('main.preprocess_job_descriptions')
    @patch('main.vectorize_text')
    @patch('main.save_embeddings')
    @patch('main.train_knn_model')
    @patch('main.find_top_k_similar_jobs')
    @patch('main.process_resume')
    def test_main(self, mock_process_resume, mock_find_top_k_similar_jobs, mock_train_knn_model,
                  mock_save_embeddings, mock_vectorize_text, mock_preprocess_job_descriptions, mock_load_data):

        # Mocking each function used in the main function
        mock_load_data.return_value = MagicMock()
        mock_preprocess_job_descriptions.return_value = ["processed_job_description"]
        mock_vectorize_text.return_value = np.array([[0.1, 0.2]])
        mock_save_embeddings.return_value = None
        mock_train_knn_model.return_value = MagicMock()
        mock_find_top_k_similar_jobs.return_value = [(0, 0.9), (1, 0.8)]
        mock_process_resume.return_value = "Software Engineer with 5 years of experience."

        result_json = main('test_resume.pdf')

        # Check if the result is in JSON format
        self.assertIn('job_title', result_json)
        self.assertIn('job_description', result_json)

if __name__ == '__main__':
    unittest.main()
