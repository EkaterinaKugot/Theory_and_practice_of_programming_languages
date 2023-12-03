import pytest
from src import SpecialDict, Token, TokenType, Number, Condition, Parser


@pytest.fixture()
def sdict_ploc():
    return SpecialDict({"value1": 1, "value2": 2, "value3": 3, "1": 10, "2": 20, "3": 30, 
                           "(1, 5)": 100, "(5, 5)": 200, "(10, 5)": 300,
                           "(1, 5, 3)": 400, "(5, 5, 4)": 500, "(10, 5, 5)": 600})

@pytest.fixture()
def sdict_iloc():
    map = SpecialDict()
    map["value1"] = 1
    map["value2"] = 2
    map["value3"] = 3
    map["1"] = 10
    map["2"] = 20
    map["3"] = 30
    map["1, 5"] = 100
    map["5, 5"] = 200
    map["10, 5"] = 300
    return map

class TestInterpreter:

    def test_iloc(self, sdict_iloc):
        assert sdict_iloc.iloc[0] == 10
        assert sdict_iloc.iloc[2] == 300  
        assert sdict_iloc.iloc[5] == 200
        assert sdict_iloc.iloc[8] == 3

    def test_incorrect_index_iloc1(self, sdict_iloc):
        with pytest.raises(ValueError):
            sdict_iloc.iloc[-1]

    def test_incorrect_index_iloc2(self, sdict_iloc):
        with pytest.raises(TypeError):
            sdict_iloc.iloc["234"]

    def test_ploc(self, sdict_ploc):
        assert sdict_ploc.ploc["<=2"] == {'1': 10, '2': 20}
        assert sdict_ploc.ploc["<3"] == {'1': 10, '2': 20}  
        assert sdict_ploc.ploc["<>0, >0"] == {'(1, 5)': 100, '(5, 5)': 200, '(10, 5)': 300}
        assert sdict_ploc.ploc[">=10, >0"] == {'(10, 5)': 300}
        assert sdict_ploc.ploc["<5, 5, =3"] == {'(1, 5, 3)': 400}

    def test_bad_token(self, sdict_ploc):
        with pytest.raises(SyntaxError):
            sdict_ploc.ploc["=9, ="]

    def test_not_valid_condition(self, sdict_ploc):
        with pytest.raises(SyntaxError):
            sdict_ploc.ploc[">   "]

    def test_condition_string(self, sdict_ploc):
        with pytest.raises(TypeError):
            sdict_ploc.ploc[123]

    def test_number_str(self):
        assert Number(Token(TokenType.NUMBER, "2")).__str__() == f"Number (Token(TokenType.NUMBER, 2))"

    def test_condition_str(self):
        assert Condition(Token(TokenType.MORE, ">"), Number(Token(TokenType.NUMBER, "2"))).__str__() \
        == f"Condition (Token(TokenType.MORE, >)Number (Token(TokenType.NUMBER, 2)))"

    def test_invalid_factor(self):
        with pytest.raises(SyntaxError):
            Parser().factor()

    def test_invalid_token_order(self):
        with pytest.raises(SyntaxError):
            Parser().check_token(TokenType.MORE)

    def test_not_dictionary(self):
        with pytest.raises(TypeError):
            SpecialDict(123)



    
