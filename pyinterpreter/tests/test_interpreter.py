import pytest
from interpreter import Interpreter, NodeVisitor, Token, TokenType, Number, BinOp, UnOp


@pytest.fixture(scope="function")
def interpreter():
    return Interpreter()

class TestInterpreter:
    interpreter = Interpreter()

    @pytest.mark.parametrize(
            "interpreter, code", [(interpreter, "2+2"),
                                  (interpreter, " 2  +     2")]
    )
    def test_add_spaces(self, interpreter, code):
        assert interpreter.eval(code) == 4
    
    def test_sub(self, interpreter):
        assert interpreter.eval("4-2") == 2

    def test_mult(self, interpreter):
        assert interpreter.eval("4*2") == 8

    def test_div(self, interpreter):
        assert interpreter.eval("4/2") == 2

    def test_paren(self, interpreter):
        assert interpreter.eval("((5-1)*(7+3))/2") == 20

    def test_unary_operator(self, interpreter):
        assert interpreter.eval("+++4   ---3") == 1
    
    def test_paren2(self, interpreter):
        with pytest.raises(SyntaxError):
            interpreter.eval("(2+3")

    def test_expr(self, interpreter):
        assert interpreter.eval("2+3*4/5") == 14.0

    def test_factor(self, interpreter):
        with pytest.raises(SyntaxError):
            interpreter.eval("2-+")

    def test_add_with_letter(self, interpreter):
        with pytest.raises(SyntaxError):
            interpreter.eval("2+a")

    def test_wrong_operator(self, interpreter):
        with pytest.raises(SyntaxError):
            interpreter.eval("2&3")
    
    def test_wrong_unary_operator(self, interpreter):
        with pytest.raises(ValueError):
            interpreter.eval("*2")

    def test_visit_binop(self, interpreter):
        with pytest.raises(ValueError):
            interpreter.visit_binop(BinOp(Number(Token(TokenType.NUMBER, 2)), Token(TokenType.OPERATOR, "^"), Number(Token(TokenType.NUMBER, 3))))

    def test_number_str(self):
        assert Number(Token(TokenType.NUMBER, "2")).__str__() == f"Number (Token(TokenType.NUMBER, 2))"

    def test_binop_str(self):
        assert (BinOp(Number(Token(TokenType.NUMBER, 2)), Token(TokenType.OPERATOR, "+"), Number(Token(TokenType.NUMBER, 3))).__str__() == 
                f"BinOp+ (Number (Token(TokenType.NUMBER, 2)), Number (Token(TokenType.NUMBER, 3)))")
        
    def test_unop_str(self):
        assert UnOp(Token(TokenType.OPERATOR, "-"), Number(Token(TokenType.NUMBER, 3))).__str__() == f"UnOp (-Number (Token(TokenType.NUMBER, 3)))"

    def test_nodevisitor(self):
        assert NodeVisitor().visit() == None


    
