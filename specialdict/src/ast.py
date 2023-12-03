from .token import Token

class Node:
    pass

class Number(Node):
    def __init__(self, token: Token):
        self.token = token

    def __str__(self):
        return f"Number ({self.token})"

class Condition(Node):
    def __init__(self, op: Token, right: Node):
        self.op = op
        self.right = right

    def __str__(self):
        return f"Condition ({self.op}{self.right})"
