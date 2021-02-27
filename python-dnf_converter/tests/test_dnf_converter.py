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
        assert test_expression.dnf_string == '(~A&B&C)|(A&~B&C)|(A&B&C)'

    def test_get_symbols_List(self):
        test_expression_string = '(A|B)&C'
        test_expression = Logic_expression(test_expression_string)
        assert test_expression.symbols_list == [symbols('A'),symbols('B'),symbols('C')]

    def test_get_symbols_symbols(self):
        test_expression_string = '(A|B)&C'
        test_expression = Logic_expression(test_expression_string)
        test_lib ={'A':symbols('A'),'B':symbols('B'),'C':symbols('C')}
        assert test_expression.used_symbols == test_lib

    def test_get_truthtable(self):
        test_expression_string = '(A|B)&C'
        test_expression = Logic_expression(test_expression_string)
        assert test_expression.truthtable == {3:True,5:True,7:True}

    def test_Truth_table(self):
        test_expression_string = '(A|B)&C'
        logic_expression_symbolic = parse_expr(test_expression_string, evaluate = False)
        symbol_dict = {'A':symbols('A'),'B':symbols('B'),'C':symbols('C')}
        test_truth_table = Truth_table(logic_expression_symbolic, symbol_dict)
        assert test_truth_table.truth_table == {0:False, 1:False, 2:False, 3:True, 4:False, 5:True, 6:False, 7:True}

    def test_create_table_entry(self):
        test_expression_string = '(A|B)&C'
        logic_expression_symbolic = parse_expr(test_expression_string, evaluate = False)
        symbol_dict = {'A':symbols('A'),'B':symbols('B'),'C':symbols('C')}
        test_truth_table = Truth_table(logic_expression_symbolic, symbol_dict)
        assert test_truth_table._create_table_entry('000') == {'A':'0','B':'0','C':'0'}
        assert test_truth_table._create_table_entry('010') == {'A':'0','B':'1','C':'0'}

    def test_evaluate_entry(self):
        test_expression_string = '(A|B)&C'
        logic_expression_symbolic = parse_expr(test_expression_string, evaluate = False)
        symbol_dict = {'A':symbols('A'),'B':symbols('B'),'C':symbols('C')}
        test_truth_table = Truth_table(logic_expression_symbolic, symbol_dict)
        assert test_truth_table._evaluate_entry({'A':'0','B':'0','C':'0'}) == False
        assert test_truth_table._evaluate_entry({'A':'1','B':'1','C':'1'}) == True

    def test
if __name__=='__main__':
    ut.main()