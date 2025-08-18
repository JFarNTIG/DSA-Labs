import pytest
from exprlib.node import Node
from exprlib.parse import parse_expression

def test_parsing_empty():
    # Test parsing an empty string.
    # Should raise ValueError.
    with pytest.raises(ValueError):
        parse_expression("")


def test_parsing_constant():
    # Test parsing and evaluating a string
    # with only a constant.
    # 2
    root: Node = parse_expression("2")
    result: float = root.evaluate()
    assert result == pytest.approx(2)


def test_parsing_simple():
    # Test parsing and evaluating a simple expression
    # with one operator.
    # 2 + 3
    root: Node = parse_expression("2 + 3")
    result: float = root.evaluate()
    assert result == pytest.approx(5)


def test_parsing_precedence_simple():
    # Test parsing and evaluating an expression where the precedence
    # of operators has an impact on the result.
    # 2 + 3 * 5
    # In this example, evaluating 2 + 3 and then multiplying by
    # 5 would be incorrect.
    # The correct order of operations is to first multiply 3 * 5,
    # and then add two.
    root: Node = parse_expression("2 + 3 * 5")
    result: float = root.evaluate()
    assert result == pytest.approx(17)


def test_parsing_parentheses_simple():
    # Test parsing and evaluating an expression with parentheses.
    # (2 + 3) * 5
    # In this example, 2 + 3 should be evaluated first, since it is in parentheses,
    # and then multiplied by 5.
    root: Node = parse_expression("(2 + 3) * 5")
    result: float = root.evaluate()
    assert result == pytest.approx(25)


def test_parsing_complex():
    # Test parsing and evaluating a complex expression where respecting
    # precedence rules and parentheses is important.
    # 27 + 22 / 11 - 37 * 31 / (6 - 7)
    root: Node = parse_expression("27 + 22 / 11 - 37 * 31 / (6 - 7)")
    result: float = root.evaluate()
    assert result == pytest.approx(1176)