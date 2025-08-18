from typing import Dict
from exprlib.node import Node

class Value(Node):
    def __init__(self, val: float):
        self.val = val
    
    def to_string(self, explicit_parens: bool = True) -> str:
        # TODO
        raise NotImplementedError("Not implemented")

    def evaluate(self, *, context: Dict[str, float] = None) -> float:
        return self.val