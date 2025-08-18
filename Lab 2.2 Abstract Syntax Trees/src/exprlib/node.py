from abc import ABC, abstractmethod
from typing import Dict

class Node(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def to_string(self, explicit_parens: bool = True) -> str:
        """Return a string representation of this expression.
        
        If `explicit_parens` is `True`, parentheses are added at the beginning and end of every binary
        operation.

        If `explicit_parens` is `False`, parentheses are only added to the string representation if
        absolutely necessary due to operator precedence.

        Example:

        ```
           *
         2   +
           3   4
        ```

        For this expression:
            - `to_string(True)` would return: `"(2 * (3 + 4))"`
            - `to_string(False)` would return: `"2 * (3 + 4)"`
        """
        pass

    @abstractmethod
    def evaluate(self, *, context: Dict[str, float] = None) -> float:
        """Evaluate this expression and return the result.

        Args
        -- 
            - context: A dict specifying the values of variables.
            For example, {'x': 3} indicates that x has the value of 3.
        
        Example
        -- 

        ```
           *
         2   +
           3   4
        ```

        For this expression:
            - `evaluate()` would return: `14`
        """
        pass