import unittest
from src.loader import load_crises, load_profiles
from src.exercise import run_exercise

class T(unittest.TestCase):
    def test_stages(self):
        c=load_crises()["cyber-disruption"]
        stages=run_exercise(c,load_profiles())
        self.assertEqual(len(stages),1+len(c.injects))

if __name__=="__main__": unittest.main()
