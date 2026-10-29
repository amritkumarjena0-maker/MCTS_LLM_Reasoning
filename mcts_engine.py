
from reasoning_node import ReasoningNode
from search_optimizer import SearchOptimizer


class MCTSEngine:
    def __init__(
        self,
        reasoner,
        iterations: int = 1000,
        max_depth: int = 3,
        exploration_constant: float = 1.414,
    ):
        self.reasoner = reasoner
        self.iterations = iterations
        self.max_depth = max_depth
        self.optimizer = SearchOptimizer(exploration_constant)

    def expand(self, node):
        if node.expanded or node.terminal:
            return

        node.expanded = True

        if node.stage >= self.max_depth:
            node.terminal = True
            return

        candidates = self.reasoner.generate_candidates(
            node.stage, node.value
        )

        candidates = self.optimizer.unique_candidates(candidates)

        for description, value in candidates:
            child = ReasoningNode(
                stage=node.stage + 1,
                value=value,
                reasoning=description,
                terminal=(node.stage + 1 >= self.max_depth),
            )
            node.add_child(child)

    def simulate(self, node):
        """
        Evaluate the current path.
        The demo uses a verifier rather than generating
        an unrestricted random rollout.
        """
        if node.stage >= self.max_depth:
            return self.reasoner.evaluate(node.value, node.stage)

        return 0.0

    def search(self):
        root = ReasoningNode(stage=0)

        for _ in range(self.iterations):
            node = root

            # 1. Selection: follow the best UCT branches.
            while (
                node.expanded
                and node.children
                and not node.terminal
            ):
                node = self.optimizer.select_best_child(node)

            # 2. Expansion: create alternative reasoning steps.
            if not node.terminal:
                self.expand(node)

                if node.children:
                    unvisited = [
                        child for child in node.children
                        if child.visits == 0
                    ]
                    if unvisited:
                        node = unvisited[0]

            # 3. Simulation / verification.
            reward = self.simulate(node)

            # 4. Backpropagation through ancestors.
            node.backpropagate(reward)

        return root

    @staticmethod
    def best_solution(root):
        """Extract the highest-reward completed path."""
        solutions = []

        def visit(node):
            if node.terminal:
                if node.visits:
                    solutions.append(node)
                return

            for child in node.children:
                visit(child)

        visit(root)

        if not solutions:
            return None

        return max(
            solutions,
            key=lambda node: (
                node.average_reward,
                node.visits,
            ),
        )
     