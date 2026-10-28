"""Speculative Decoding Acceptance & Rejection Engine."""
import random
from typing import List, Tuple

class SpeculativeEngine:
    def __init__(self, acceptance_threshold: float = 0.85):
        self.threshold = acceptance_threshold

    def evaluate_draft(self, draft_tokens: List[int], target_probs: List[float], draft_probs: List[float]) -> Tuple[List[int], int]:
        accepted = []
        for i, tok in enumerate(draft_tokens):
            p_target = target_probs[i]
            p_draft = draft_probs[i]
            alpha = min(1.0, p_target / max(1e-6, p_draft))
            if random.random() <= alpha:
                accepted.append(tok)
            else:
                break
        return accepted, len(accepted)
