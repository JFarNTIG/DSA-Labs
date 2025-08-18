from exprlib.node import Node
from exprlib.parse import parse_expression

print("Hi! Welcome to my math parsing app.")

expr_text: str = input("Enter a math expression: ")
root: Node = parse_expression(expr_text)
result: float = root.evaluate()
print("The result is:", result)