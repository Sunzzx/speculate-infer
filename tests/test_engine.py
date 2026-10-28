import unittest
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))
from speculate_infer.engine import SpeculativeEngine

class TestSpeculate(unittest.TestCase):
    def test_acceptance_criteria(self):
        engine = SpeculativeEngine()
        tokens = [101, 204, 305]
        target_p = [0.9, 0.95, 0.9]
        draft_p = [0.8, 0.9, 0.85]
        acc, count = engine.evaluate_draft(tokens, target_p, draft_p)
        self.assertGreater(count, 0)

if __name__ == "__main__":
    unittest.main()
