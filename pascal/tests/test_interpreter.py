import pytest
from interpreter import Interpreter, NodeVisitor, Token, TokenType, Parser
from interpreter import Number, BinOp, UnOp, Variable, Assignment, Empty, Semicolon


@pytest.fixture(scope="function")
def interpreter():
    return Interpreter()

class TestInterpreter:
    interpreter = Interpreter()

    def test_first_program(self, interpreter):
        assert interpreter.eval("BEGIN END.") == {}

    def test_second_program(self, interpreter):
        assert interpreter.eval("BEGIN x:= 2 + 3 * (2 + 3); y:= 2 / 2 - 2 + 3 * ((1 + 1) + (1 + 1)); END.") == {'x': 17.0, 'y': 11.0}

    def test_threed_program(self, interpreter):
        assert interpreter.eval(
            "BEGIN y: = 2; BEGIN a := 3; a := a; b := -10 ++ a + 10 * y / 4; c := a - b END; x := 11; END."
            ) == {'y': 2.0, 'a': 3.0, 'b': -2.0, 'c': 5.0, 'x': 11.0}
        
    def test_invalid_token_order(self, interpreter):
        with pytest.raises(SyntaxError):
            interpreter.eval("x")

    def test_bad_token(self, interpreter):
        with pytest.raises(SyntaxError):
            interpreter.eval("BEGIN a : 3")

    def test_invalid_factor(self):
        with pytest.raises(SyntaxError):
            Parser().factor()
    
    def test_invalid_statement(self):
        with pytest.raises(SyntaxError):
            Parser().statement()

    def test_uninitialized_variable(self, interpreter):
        with pytest.raises(ValueError):
            interpreter.eval("BEGIN a := b END.")
    
    def test_invalid_unary_operator(self, interpreter):
        with pytest.raises(ValueError):
            interpreter.visit_unop(UnOp(Token(TokenType.OPERATOR, "^"), Number(Token(TokenType.NUMBER, 2))))

    def test_invalid_operator(self, interpreter):
        with pytest.raises(ValueError):
            interpreter.visit_binop(BinOp(Number(Token(TokenType.NUMBER, 2)), Token(TokenType.OPERATOR, "^"), Number(Token(TokenType.NUMBER, 3))))

    def test_number_str(self):
        assert Number(Token(TokenType.NUMBER, "2")).__str__() == f"Number (Token(TokenType.NUMBER, 2))"

    def test_binop_str(self):
        assert (BinOp(Number(Token(TokenType.NUMBER, 2)), Token(TokenType.OPERATOR, "+"), Number(Token(TokenType.NUMBER, 3))).__str__() == 
                f"BinOp+ (Number (Token(TokenType.NUMBER, 2)), Number (Token(TokenType.NUMBER, 3)))")
        
    def test_unop_str(self):
        assert UnOp(Token(TokenType.OPERATOR, "-"), Number(Token(TokenType.NUMBER, 3))).__str__() == f"UnOp (-Number (Token(TokenType.NUMBER, 3)))"

    def test_variable_str(self):
        assert Variable(Token(TokenType.ID, "x")).__str__() == f"Var (Token(TokenType.ID, x))"

    def test_assignment_str(self):
        assert Assignment(Variable(Token(TokenType.ID, "x")), Token(TokenType.NUMBER, "3")).__str__() == "Assignment (Var (Token(TokenType.ID, x)) = Token(TokenType.NUMBER, 3))"
    
    def test_empty_str(self):
        assert Empty().__str__() == "Empty ()"

    def test_semicolon_str(self):
        assert Semicolon(Token(TokenType.NUMBER, "3"), Token(TokenType.NUMBER, "4")).__str__() == "Semicolon (Token(TokenType.NUMBER, 3), Token(TokenType.NUMBER, 4))"

    def test_nodevisitor(self):
        assert NodeVisitor().visit() == None


    
