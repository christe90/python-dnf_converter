import unittest as ut
from dnf_converter.cli import main
from dnf_converter.dnf_converter import *
from sympy import *

class TestDnfConverter(ut.TestCase):
    def test_main(self):
        assert main([]) == 0
    
    def test_Logic_expression(self):
        test_expression_string = '(A|B)&C'
        test_expression = Logic_expression(test_expression_string)
        assert test_expression.dnf_string == '(A&~B&C)|(A&B&C)|(~A&B&C)'

    def test_get_symbols_List(self):
        test_expression_string = '(A|B)&C'
        test_expression = Logic_expression(test_expression_string)
        assert test_expression.symbols_list == ['A','B','C']

    def test_get_symbols_symbols(self):
        test_expression_string = '(A|B)&C'
        test_expression = Logic_expression(test_expression_string)
        test_lib ={'A':symbols('A'),'B':symbols('B'),'C':symbols('C')}
        assert test_expression.used_symbols == test_lib

    def test_get_truthtable(self):
        test_expression_string = '(A|B)&C'
        test_expression = Logic_expression(test_expression_string)
        assert test_expression.truthtable == {5:True,6:True,7:True}

if __name__=='__main__':
    ut.main()