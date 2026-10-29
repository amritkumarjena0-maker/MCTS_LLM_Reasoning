
from dataclasses import dataclass, field
from typing import Optional


@dataclass
class ReasoningNode:
    stage: int
    value: Optional[float] = None
    reasoning: str = ""
    parent: Optional["ReasoningNode"] = field(
        default=None, repr=False, compare=False
    )
    children: list["ReasoningNode"] = field(default_factory=list)
    visits: int = 0
    total_reward: float = 0.0
    terminal: bool = False
    expanded: bool = False

    @property
    def average_reward(self) -> float:
        return self.total_reward / self.visits if self.visits else 0.0

    def add_child(self, child: "ReasoningNode") -> None:
        child.parent = self
        self.children.append(child)

    def backpropagate(self, reward: float) -> None:
        """Update this node and every ancestor."""
        node = self
        while node is not None:
            node.visits += 1
            node.total_reward += reward
            node = node.parent

    def path(self) -> list["ReasoningNode"]:
        """Return the path from the root to this node."""
        result = []
        node = self

        while node is not None:
            result.append(node)
            node = node.parent

        return list(reversed(result))
