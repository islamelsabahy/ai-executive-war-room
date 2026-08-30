import unittest
from src.loader import load_crises, load_profiles
from src.agents import run_agents

class T(unittest.TestCase):
    def test_five_agents(self):
        views=run_agents(load_crises()["platform-outage"],load_profiles())
        self.assertEqual(len(views),5)
        self.assertTrue(all(v.recommendation for v in views))

if __name__=="__main__": unittest.main()
