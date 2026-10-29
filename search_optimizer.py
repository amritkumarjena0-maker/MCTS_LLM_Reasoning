
import math


class SearchOptimizer:
    def __init__(self, exploration_constant: float = 1.414):
        self.exploration_constant = exploration_constant

    def uct_score(self, child, parent_visits: int) -> float:
        """Upper Confidence Bound for Trees (UCT)."""
        if child.visits == 0:
            return float("inf")

        exploitation = child.average_reward
        exploration = self.exploration_constant * math.sqrt(
            math.log(max(parent_visits, 1)) / child.visits
        )

        return exploitation + exploration

    def select_best_child(self, node):
        if not node.children:
            return None

        return max(
            node.children,
            key=lambda child: self.uct_score(child, node.visits),
        )

    @staticmethod
    def unique_candidates(candidates):
        """Remove candidates with duplicate resulting values."""
        seen = set()
        unique = []

        for description, value in candidates:
            if value not in seen:
                seen.add(value)
                unique.append((description, value))

        return unique
