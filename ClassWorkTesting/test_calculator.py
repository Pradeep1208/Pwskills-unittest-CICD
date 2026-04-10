# test code by this command --> python -m unittest test_calculator.py
# unittest test_calculator.py

import unittest
from calculator import Calculator
class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()
        
    def test_add(self):
        self.assertEqual(10,self.calc.add(5,5))
        
    def test_subs(self):
        self.assertEqual(2,self.calc.subs(5,3))
        
    def test_divide(self):
        self.assertEqual(2.0, self.calc.divide(10,5))
        
    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            self.calc.divide(10,0)
            
            
if __name__ == "__main__":
    unittest.main()




# from calculator import Calculator
# import pytest

# class TestCalculator:
#     def setup_method(self):
#         self.cacl = Calculator()
        
#     def test_add(self):
#         assert self.calc.add(2, 3) == 5
        
#     def test_subs(self):
#         assert self.calc.subs(5,3) == 2
        
#     def test_divide(self):
#         assert self.cacl.divide(10,2) == 5
        
#     def test_divide_by_zero(self):
#         with pytest.raises(ValueError):
#             self.cacl.divide(10,0)