import unittest
from matching_algorithm.utils.vectorization import vectorize_text

class TestVectorization(unittest.TestCase):

    def test_vectorize_text(self):
        text = ["Software Engineer with experience in AI", "Data Scientist proficient in Python"]
        embeddings = vectorize_text(text)

        # Check if the embeddings are a numpy array and not empty
        self.assertIsInstance(embeddings, np.ndarray)
        self.assertGreater(embeddings.shape[0], 0)  # Ensure that embeddings are returned for each input text

if __name__ == '__main__':
    unittest.main()
