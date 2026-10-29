
# MCTS for Multi-Step LLM Reasoning

## Description
A Python implementation of Monte Carlo Tree Search for multi-step reasoning, with UCT selection, backtracking through alternative reasoning paths, reward-based verification, and duplicate-state pruning.

## Features
- Monte Carlo Tree Search (MCTS)
- Upper Confidence Bound for Trees (UCT)
- Multi-step reasoning paths
- Alternative candidate exploration
- Backpropagation of rewards
- Backtracking through search-tree branches
- Duplicate-state pruning
- Verifier-based answer evaluation
- Pluggable reasoning engine for future LLM integration

## Technologies
- Python
- Object-oriented programming
- Monte Carlo Tree Search
- Tree search optimization

## Requirements
Python 3.10 or newer.

## How to Run
Run the following command from the project folder:

    python main.py

## Algorithm
1. Initialize the root reasoning node.
2. Select a promising node using UCT.
3. Expand the node with alternative reasoning steps.
4. Evaluate completed reasoning paths.
5. Backpropagate rewards through parent nodes.
6. Explore alternative branches when earlier paths perform poorly.
7. Return the highest-reward completed solution.

## Flowchart

    Start
      |
      v
    Initialize MCTS Tree
      |
      v
    Select Node Using UCT
      |
      v
    Expand Candidate Steps
      |
      v
    Evaluate Reasoning Path
      |
      v
    Backpropagate Reward
      |
      v
    More Iterations?
      | Yes
      +----------> Select Node
      |
      No
      v
    Select Best Verified Path
      |
      v
    Display Answer
      |
      v
    End

## Note
The included reasoning engine is a deterministic demonstration, not a connected LLM. Replace its candidate generator and evaluator with an actual language model and suitable verification logic to apply MCTS to open-ended reasoning tasks.
