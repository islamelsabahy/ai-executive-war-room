import unittest
from src.loader import load_crises, load_profiles
from src.agents import run_agents
from src.council import synthesize

class T(unittest.TestCase):
    def test_decision(self):
        c=load_crises()["platform-outage"]
        d=synthesize(c,run_agents(c,load_profiles()))
        self.assertIn(d.recommended_option,{o["id"] for o in c.options})
        self.assertGreaterEqual(d.consensus_score,0)
        self.assertLessEqual(d.consensus_score,100)
        self.assertTrue(d.red_team_challenges)

if __name__=="__main__": unittest.main()
