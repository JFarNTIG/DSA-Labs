from exprlib.node import Node

def contains_op(root: Node, op: str) -> bool:
    """Returns True if an expression contains a given operator,
    otherwise False.

    Examples:
        - Does `2 + 3 * 5` contain `+`? -> `True`
        - Does `2 + 3 * 5` contain `/`? -> `False`
    """
    # TODO
    raise NotImplementedError("Not implemented")


def contains_value(root: Node, val: float) -> bool:
    """Returns True if an expression contains a given value,
    otherwise False.

    Examples:
        - Does `2 + 3 * 5` contain `5`? -> `True`
        - Does `2 + 3 * 5` contain `7`? -> `False`
    """
    # TODO
    raise NotImplementedError("Not implemented")
