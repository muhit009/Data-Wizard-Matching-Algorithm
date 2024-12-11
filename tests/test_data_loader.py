import unittest
from matching_algorithm.utils.data_loader import load_data
import pandas as pd
from unittest.mock import patch, MagicMock

class TestDataLoader(unittest.TestCase):

    @patch('pandas.read_csv')
    def test_load_data(self, mock_read_csv):
        # Mocking the CSV file reading process
        mock_data1 = pd.DataFrame({
            "Job Title": ["Software Engineer", "Data Scientist"],
            "Job Description": ["Description 1", "Description 2"]
        })
        mock_data2 = pd.DataFrame({
            "position_title": ["Project Manager", "UX Designer"],
            "job_description": ["Description 3", "Description 4"]
        })
        mock_read_csv.side_effect = [mock_data1, mock_data2]  # Simulate reading both datasets

        data = load_data()

        # Check if the combined data is correct
        self.assertEqual(data.shape[0], 4)  # 4 combined records
        self.assertTrue("Job Title" in data.columns)
        self.assertTrue("Job Description" in data.columns)

    @patch('pandas.read_csv')
    def test_filter_short_descriptions(self, mock_read_csv):
        # Mocking the CSV file reading process
        mock_data1 = pd.DataFrame({
            "Job Title": ["Software Engineer"],
            "Job Description": ["Short description"]
        })
        mock_data2 = pd.DataFrame({
            "position_title": ["Project Manager"],
            "job_description": ["A very long description" * 50]  # Longer than 600 characters
        })
        mock_read_csv.side_effect = [mock_data1, mock_data2]  # Simulate reading both datasets

        data = load_data()

        # Check that the short description was filtered out
        self.assertEqual(data.shape[0], 1)
        self.assertEqual(data.iloc[0]["Job Title"], "Project Manager")

if __name__ == '__main__':
    unittest.main()
