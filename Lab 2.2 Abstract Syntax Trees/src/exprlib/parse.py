from typing import List
from exprlib.node import Node
from exprlib.value import Value
from exprlib.binop import BinaryOp

def _tokenize(expr: str) -> List[str]:
    """
    Convert an infix expression string into a list of tokens.
    Tokens are: numbers ('12', '3.14'), operators ('+','-','*','/'), or
    parentheses ('(', ')'). Whitespace is ignored.
    """
    tokens: List[str] = []
    num_buffer: List[str] = []

    def flush_number():
        if num_buffer:
            tokens.append(''.join(num_buffer))
            num_buffer.clear()

    for ch in expr:
        if ch.isspace():
            continue
        elif ch.isdigit() or ch == '.':
            num_buffer.append(ch)
        elif ch in "+-*/()":
            flush_number()
            tokens.append(ch)
        else:
            raise ValueError(f"Unexpected character: {ch}")

    flush_number()
    return tokens

_PRECEDENCE = {
    '+': 1,
    '-': 1,
    '*': 2,
    '/': 2
}

def _apply_operator(op_stack: List[str], out_stack: List[Node]):
    """
    Pop one operator from op_stack, build a BinaryOp from the two top
    nodes on out_stack, and push the new node back.
    """
    op = op_stack.pop()
    try:
        right = out_stack.pop()
        left  = out_stack.pop()
    except IndexError:
        raise ValueError("Parse error: Missing operand")
    
    out_stack.append(BinaryOp(op, left, right))

def parse_expression(expr: str) -> Node:
    """
    Parse an arithmetic expression containing +, -, *, / and parentheses,
    returning the root of a syntax tree made of Value and BinaryOp nodes.
    """
    output: List[Node] = []
    ops: List[str] = []

    for tok in _tokenize(expr):
        if tok[0].isdigit():
            output.append(Value(float(tok)))
        elif tok in _PRECEDENCE:
            while (ops and ops[-1] in _PRECEDENCE and
                   _PRECEDENCE[ops[-1]] >= _PRECEDENCE[tok]):
                _apply_operator(ops, output)
            ops.append(tok)
        elif tok == '(':
            ops.append(tok)
        elif tok == ')':
            while ops and ops[-1] != '(':
                _apply_operator(ops, output)
            if not ops:
                raise ValueError("Mismatched parentheses")
            ops.pop()
        else:
            raise ValueError(f"Unknown token: {tok}")

    while ops:
        if ops[-1] == '(':
            raise ValueError("Mismatched parentheses")
        _apply_operator(ops, output)

    if len(output) != 1:
        raise ValueError("Malformed expression")
    return output[0]