from .token import Token, TokenType

class Lexer():

    def __init__(self):
        self._pos = 0
        self._text = ""
        self._current_char = None

    def init(self, text):
        self._text = text
        self._pos = 0
        self._current_char = self._text[self._pos]

    def forward(self):
        self._pos += 1
        if self._pos > len(self._text) - 1:
            self._current_char = None
        else:
            self._current_char = self._text[self._pos]

    def skip(self):
        while (self._current_char and 
               self._current_char not in ['>', '<', '=', '.'] and
               not self._current_char.isdigit()):
            self.forward()

    def number(self):
        result  = []
        while (self._current_char and 
               (self._current_char.isdigit() or
                self._current_char == ".")):
            result.append(self._current_char)
            self.forward()
        return "".join(result)
    
    def operators(self):
        result = self._current_char 
        self.forward()
        if (self._current_char and self._current_char == '='):
            result += self._current_char
            if result[0] == '>':
                token_type = TokenType.MOREEQUAL
            elif result[0] == '<':
                token_type = TokenType.LESSEQUAL
            self.forward()
        elif (self._current_char and result == '<' and self._current_char == '>'):
            result += self._current_char
            token_type = TokenType.UNEQUAL
            self.forward()
            
        if (self._current_char and self._current_char.isdigit()):
            if result == '>':
                token_type = TokenType.MORE
            elif result == '<':
                token_type = TokenType.LESS
        else:
            raise SyntaxError("Not a valid condition")
        return Token(token_type, result)


    def next(self):
        while self._current_char:
            if (self._current_char not in ['>', '<', '='] and
                not self._current_char.isdigit()):
                self.skip()
                continue
            if self._current_char.isdigit():
                return Token(TokenType.NUMBER, self.number())
            if self._current_char in ['>', '<']:
                return self.operators() 
            if self._current_char == '=':
                res = self._current_char
                self.forward()
                if(self._current_char and self._current_char.isdigit()):
                    return Token(TokenType.EQUAL, res)
            raise SyntaxError("bad token")

    

    