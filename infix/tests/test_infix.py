import pytest
from infix import to_infix, start
from unittest.mock import patch

@pytest.mark.parametrize(
        "str1, infix",
        [("+ - 13 4 55", "((13 - 4) + 55)"),
         ("+ 2 * 2 - 2 1", "(2 + (2 * (2 - 1)))"),
         ("/ + 3 10 * + 2 3 - 3 5", "((3 + 10) / ((2 + 3) * (3 - 5)))"),]
        )
def test_to_infix(str1, infix):
    assert to_infix(str1) == infix

def test_input():
      with patch('builtins.input', return_value='- 1 1'):
            assert start() == 'Infix expression: (1 - 1)'

def test_to_infix_raises():
    with pytest.raises(TypeError):
            to_infix("+ - 13 4 55 y")
    with pytest.raises(ValueError):
            to_infix("- - 1 2")
    with pytest.raises(ValueError):
            to_infix("* 2 6 + 3")
