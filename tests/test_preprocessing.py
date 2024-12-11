import unittest
from matching_algorithm.utils.preprocessing import clean_job_descriptions, further_preprocessing

class TestPreprocessing(unittest.TestCase):

    def test_clean_job_descriptions(self):
        raw_description = "Contact: john.doe@gmail.com. Responsibilities include coding and developing."
        cleaned_description = clean_job_descriptions(raw_description)

        # Check if email and unwanted characters are removed
        self.assertNotIn('john.doe@gmail.com', cleaned_description)
        self.assertNotIn('coding', cleaned_description)
        self.assertIn('responsibilities', cleaned_description)

    def test_further_preprocessing(self):
        raw_text = "The responsibilities include managing, analyzing, and overseeing."
        processed_text = further_preprocessing(raw_text)

        # Check if unwanted line breaks and extra spaces are removed
        self.assertEqual(processed_text, "The responsibilities include managing, analyzing, and overseeing.")

if __name__ == '__main__':
    unittest.main()
