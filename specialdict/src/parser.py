from .token import Token, TokenType
from .lexer import Lexer
from .ast import Number, Condition

class Parser:
    def __init__(self):
        self._current_token = None
        self._lexer = Lexer()

    def check_token(self, type_: TokenType):
        if self._current_token is not None and self._current_token.type_ == type_:
            self._current_token = self._lexer.next()
        else:
            raise SyntaxError("Invalid token order")
    
    def factor(self):
        token = self._current_token
        if token:
            if token.type_ == TokenType.NUMBER:
                self.check_token(TokenType.NUMBER)
                return Number(token)
            if token.type_ in [TokenType.MORE, TokenType.LESS, TokenType.MOREEQUAL,
                               TokenType.LESSEQUAL, TokenType.EQUAL, TokenType.UNEQUAL]:
                self.check_token(token.type_)
                return Condition(token, self.factor())
        raise SyntaxError("Invalid factor")
    
    def next(self):
        result = []
        while self._current_token:
            res = self.factor()
            if isinstance(res, Number):
                res = Condition(Token(TokenType.EQUAL, '='), res)
            result.append(res)
        return result

    
    def parse(self, cond):
        self._lexer.init(cond)
        self._current_token = self._lexer.next()
        return self.next()