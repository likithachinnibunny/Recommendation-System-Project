import unittest
from recommender import recommend_movies

class TestRecommender(unittest.TestCase):

    def test_valid_genre(self):
        result = recommend_movies("Action")
        self.assertTrue(len(result) > 0)

    def test_invalid_genre(self):
        result = recommend_movies("Sci-Fi")
        self.assertEqual(result, [])

if __name__ == "__main__":
    unittest.main()
