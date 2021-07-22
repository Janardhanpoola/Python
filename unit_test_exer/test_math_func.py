#from unit_test_exer.math_func import *
# from . import math_func

from math_func import *

import pytest

@pytest.mark.numbers

def test_add():
    assert add(4,5)==9
    
@pytest.mark.numbers
def test_prod():
    assert mul(5,8)==40
    assert mul(4)==360

@pytest.mark.skip(reason="dont run test strings")

def test_strings():
    result=add('H','W')
    assert add('Hello','world')=='Helloworld'
    assert result=='HW'
    assert type(result) is str
    assert 'ok' in result

