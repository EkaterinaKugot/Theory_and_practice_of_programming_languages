from .parser import Parser
from .token import Token, TokenType
from .ast import Number, Condition

def operator(cond: Condition, num: Token):
    if cond.op.value == '>':
        return int(num.value) > int(cond.right.token.value)
    elif cond.op.value == '<':
        return int(num.value) < int(cond.right.token.value)
    elif cond.op.value == '>=':
        return int(num.value) >= int(cond.right.token.value)
    elif cond.op.value == '<=':
        return int(num.value) <= int(cond.right.token.value)
    elif cond.op.value == '=':
        return int(num.value) == int(cond.right.token.value)
    elif cond.op.value == '<>':
        return int(num.value) != int(cond.right.token.value)

class Ploc(dict):
    def __init__(self, dictionary: dict):
        self.sdict = dictionary
        self.parser = Parser()
    
    def __getitem__(self, cond):
        if not isinstance(cond, str):
            raise TypeError("The condition must be a string")
        tree = self.parser.parse(cond)
        size = len(tree)
        list_keys = []
        for k in list(self.sdict.keys()):
            if k.isdigit() or (k[0] == '(' and k[-1] == ')'):
                res = self.parser.parse(k)
                if len(res) == size:
                    list_keys.append([k, res])
        result = {}
        for i in list_keys:
            count = 0
            for j in range(len(i[1])):
                if operator(tree[j], i[1][j].right.token):
                    count += 1
            if count == size:
                result[i[0]] = self.sdict[i[0]]

        return result
        