from .token import Token

class Node:
    pass

class Number(Node):
    def __init__(self, token: Token):
        self.token = token

    def __str__(self):
        return f"Number ({self.token})"

class BinOp(Node):
    def __init__(self, left: Node, op: Token, right: Node):
        self.left = left
        self.op = op
        self.right = right

    def __str__(self):
        return f"BinOp{self.op.value} ({self.left}, {self.right})"
    

class UnOp(Node):
    def __init__(self, op: Token, right: Node):
        self.op = op
        self.right = right

    def __str__(self):
        return f"UnOp ({self.op.value}{self.right})"
    
class Variable(Node):
    def __init__(self, token: Token):
        self.token = token

    def __str__(self):
        return f"Var ({self.token})"
    
class Assignment(Node):
    def __init__(self, var: Variable, value: Node):
        self.var = var
        self.value = value

    def __str__(self):
        return f"Assignment ({self.var} = {self.value})"
    
class Empty(Node):
    def __init__(self):
        self.token = ''

    def __str__(self):
        return f"Empty ({self.token})"
    
class Semicolon(Node):
    def __init__(self, left: Node, right: Node):
        self.left = left
        self.right = right

    def __str__(self):
        return f"Semicolon ({self.left}, {self.right})"
    

