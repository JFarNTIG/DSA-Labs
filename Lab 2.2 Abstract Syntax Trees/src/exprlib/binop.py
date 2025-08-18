from typing import Dict
from exprlib.node import Node

class BinaryOp(Node):
    def __init__(self, op: str, left: Node, right: Node):
        self.op = op
        self.left = left
        self.right = right
    
    def to_string(self, explicit_parens: bool = True) -> str:
        # TODO
        raise NotImplementedError("Not implemented")

    def evaluate(self, *, context: Dict[str, float] = None) -> float:
        if self.op == '+':
            return self.left.evaluate() + self.right.evaluate()
        elif self.op == '-':
            return self.left.evaluate() - self.right.evaluate()
        elif self.op == '*':
            return self.left.evaluate() * self.right.evaluate()
        elif self.op == '/':
            return self.left.evaluate() / self.right.evaluate()