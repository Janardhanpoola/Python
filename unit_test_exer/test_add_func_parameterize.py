
import pytest

from add_func import *



@pytest.mark.parametrize( 'num1,num2,result',
                             
                             [
                                 (89,90,179),
                                 ('hello','world','helloworld')

                             ]


                          )
def test_add(num1,num2,result):
    assert add(num1,num2)==result