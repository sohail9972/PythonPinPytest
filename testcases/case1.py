import pytest;
import Source.first_testcase as first_tescases


def test_add():
    result = first_tescases.adding(5,9)
    assert result==14

def test_add_Strings():
    result= first_tescases.adding("i like ","icecream")
    assert result == "i like icecream"

    
def test_divide():
    result = first_tescases.divide(10,2)
    assert result==5


def test_divide_byzero():
    # with pytest.raises(ZeroDivisionError):
  with pytest.raises(ValueError):
        first_tescases.divide(10,0)
    # assert True