import unittest
from src.loader import load_crises, load_profiles
from src.comparison import compare_options

class T(unittest.TestCase):
    def test_ranking(self):
        data=compare_options(load_crises()["customer-trust"],load_profiles())
        self.assertGreaterEqual(len(data["ranking"]),2)
        self.assertEqual(len(data["role_votes"]),5)

if __name__=="__main__": unittest.main()
