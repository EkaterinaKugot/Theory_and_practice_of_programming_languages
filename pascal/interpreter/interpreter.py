from .parser import Parser
from .ast import BinOp, Number, UnOp, Variable, Assignment, Empty, Semicolon

class NodeVisitor:
    
    def visit(self):
        pass

class Interpreter(NodeVisitor):
    
    def __init__(self):
        self.parser = Parser()
        self.value_variables = {}

    def visit(self, node):
        if isinstance(node, Number):
            return self.visit_number(node)
        elif isinstance(node, BinOp):
            return self.visit_binop(node)
        elif isinstance(node, UnOp):
            return self.visit_unop(node)
        elif isinstance(node, Variable):
            return self.visit_variable(node)
        elif isinstance(node, Assignment):
            return self.visit_assignment(node)
        elif isinstance(node, Empty):
            return self.visit_empty()
        elif isinstance(node, Semicolon):
            return self.visit_semicolon(node)
        

    def visit_number(self, node):
        return float(node.token.value)

    def visit_binop(self, node):
        match node.op.value:
            case "+":
                return self.visit(node.left) + self.visit(node.right)
            case "-":
                return self.visit(node.left) - self.visit(node.right)
            case "*":
                return self.visit(node.left) * self.visit(node.right)
            case "/":
                return self.visit(node.left) / self.visit(node.right)
            case _:
                raise ValueError("Invalid operator")
            
    def visit_unop(self, node):
        match node.op.value:
            case "+":
                return self.visit(node.right)
            case "-":
                return self.visit(node.right) * (-1)
            case _:
                raise ValueError("Invalid unary operator")
            
    def visit_variable(self, node):
        if node.token.value in self.value_variables.keys():
            return self.value_variables[node.token.value]
        raise ValueError(f"Uninitialized variable {node.token.value}")

    def visit_assignment(self, node):
        if node.var.value not in self.value_variables.keys():
            self.value_variables[node.var.value] = 0
        self.value_variables[node.var.value] = self.visit(node.value)

    def visit_empty(self):
        return ''

    def visit_semicolon(self, node):
        self.visit(node.left)
        self.visit(node.right)

    def eval(self, code):
        tree = self.parser.parse(code)
        self.visit(tree)
        return self.value_variables
