import pytest
from exprlib.node import Node
from exprlib.parse import parse_expression
from exprlib.utils import contains_op, contains_value

def test_contains_op_simple():
    root: Node = parse_expression("2 + 3")
    assert contains_op(root, '+') == True
    assert contains_op(root, '-') == False

def test_contains_op_complex():
    root: Node = parse_expression("27 + 3 * 2 - 37 * (1 + 7)")
    assert contains_op(root, '+') == True
    assert contains_op(root, '-') == True
    assert contains_op(root, '*') == True
    assert contains_op(root, '/') == False

def test_contains_value_simple():
    root: Node = parse_expression("2 + 3")
    assert contains_value(root, 3) == True
    assert contains_value(root, 2) == True
    assert contains_value(root, 6) == False
    assert contains_value(root, 0) == False

def test_contains_value_complex():
    root: Node = parse_expression("27 + 3 * 2 - 37 * (1 + 7)")
    assert contains_value(root, 27) == True
    assert contains_value(root, 37) == True
    assert contains_value(root, 1) == True
    assert contains_value(root, 6) == False
    assert contains_value(root, 0) == False
    assert contains_value(root, -263) == False