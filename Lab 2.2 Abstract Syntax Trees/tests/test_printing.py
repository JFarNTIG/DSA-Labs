import pytest
from exprlib.node import Node
from exprlib.parse import parse_expression

def test_printing_constant_explicit():
    root: Node = parse_expression("2")
    result: str = root.to_string(True)
    assert result == "2"
    

def test_printing_simple_explicit():
    root: Node = parse_expression("2 + 3")
    result: str = root.to_string(True)
    assert result == "(2 + 3)"


def test_printing_precedence_explicit():
    root: Node = parse_expression("2 + 3 * 5")
    result: str = root.to_string(True)
    assert result == "(2 + (3 * 5))"


def test_printing_parentheses_explicit():
    root: Node = parse_expression("(2 + 3) * 5")
    result: str = root.to_string(True)
    assert result == "((2 + 3) * 5)"


def test_printing_natural():
    root: Node = parse_expression("2 + 3")
    result: str = root.to_string(False)
    assert result == "2 + 3"


def test_printing_precedence_natural():
    root: Node = parse_expression("2 + 3 * 5")
    result: str = root.to_string(False)
    assert result == "2 + 3 * 5"


def test_printing_parentheses_natural():
    root: Node = parse_expression("(2 + 3) * 5")
    result: str = root.to_string(False)
    assert result == "(2 + 3) * 5"


def test_printing_complex_natural():
    root: Node = parse_expression("27 + 22 / 11 - 37 * 31 / (6 - 7)")
    result: str = root.to_string(False)
    assert result == "27 + 22 / 11 - 37 * 31 / (6 - 7)"