import unittest
from src.loader import load_crises, load_profiles
from src.agents import run_agents
from src.red_team import challenge

class T(unittest.TestCase):
    def test_low_evidence_challenge(self):
        c=load_crises()["cyber-disruption"]
        views=run_agents(c,load_profiles())
        result=challenge(c,views,views[0].recommendation)
        self.assertGreaterEqual(len(result),1)

if __name__=="__main__": unittest.main()
