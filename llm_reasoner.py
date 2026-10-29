
class LLMReasoner:
    """
    Replace this demo reasoning engine with a real LLM later.

    Task:
        Calculate (18 + 6) * 3 - 10

    Each candidate contains:
        explanation, resulting value
    """

    def __init__(self):
        self.stages = [
            {
                "operation": "18 + 6",
                "candidates": [
                    ("Add 18 and 6 correctly.", 24),
                    ("Addition error: 18 + 6 = 25.", 25),
                    ("Addition error: 18 + 6 = 23.", 23),
                ],
            },
            {
                "operation": "previous value * 3",
                "candidates": [
                    ("Multiply the previous value by 3.", None),
                    ("Incorrect multiplication.", None),
                ],
            },
            {
                "operation": "previous value - 10",
                "candidates": [
                    ("Subtract 10 from the previous value.", None),
                    ("Incorrect subtraction.", None),
                ],
            },
        ]

    def generate_candidates(self, stage: int, value=None):
        if stage == 0:
            return [
                (description, result)
                for description, result in
                self.stages[0]["candidates"]
            ]

        if stage == 1:
            if value is None:
                return []

            return [
                ("Multiply by 3 correctly.", value * 3),
                ("Explore an incorrect multiplication.", value * 3 + 3),
            ]

        if stage == 2:
            if value is None:
                return []

            return [
                ("Subtract 10 correctly.", value - 10),
                ("Explore an incorrect subtraction.", value - 8),
            ]

        return []

    def evaluate(self, value, stage: int) -> float:
        """Reward correct completed reasoning paths."""
        if stage < len(self.stages):
            return 0.0

        return 1.0 if value == 62 else 0.0
