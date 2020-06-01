import unittest

class Calculator:
    def add(self,x,y):
        return 'Nothing'

class test_calc_add(unittest.TestCase):
 
    def test_calculator_add_method_returns_correct_result(self):
        calc = Calculator()
        result = calc.add(2,2)
        self.assertEqual(4, result)

if __name__ == '__main__':
    unittest.main()