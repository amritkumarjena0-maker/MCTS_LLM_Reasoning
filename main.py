
from llm_reasoner import LLMReasoner
from mcts_engine import MCTSEngine


def main():
    print("=" * 60)
    print("MCTS FOR MULTI-STEP LLM REASONING")
    print("=" * 60)

    problem = "(18 + 6) * 3 - 10"
    print(f"\nProblem: Calculate {problem}")
    print("Search: Monte Carlo Tree Search with UCT")
    print("Backtracking: Enabled")
    print("Optimization: Duplicate-state pruning")

    reasoner = LLMReasoner()

    engine = MCTSEngine(
        reasoner=reasoner,
        iterations=1000,
        max_depth=3,
        exploration_constant=1.414,
    )

    root = engine.search()
    solution = engine.best_solution(root)

    print("\n" + "-" * 60)
    print("SEARCH RESULTS")
    print("-" * 60)

    if solution is None:
        print("No completed reasoning path was found.")
        return

    print(f"Iterations: {engine.iterations}")
    print(f"Best path visits: {solution.visits}")
    print(f"Verified reward: {solution.average_reward:.2f}")

    print("\nSelected reasoning path:")

    for index, node in enumerate(solution.path()):
        if index == 0:
            print("Start: Original problem")
        else:
            print(f"Step {index}: {node.reasoning}")
            print(f"        Intermediate value: {node.value}")

    print(f"\nFinal answer: {solution.value}")
    print(f"Expected answer: 62")
    print(
        "Status:",
        "CORRECT" if solution.value == 62 else "INCORRECT",
    )


if __name__ == "__main__":
    main()
