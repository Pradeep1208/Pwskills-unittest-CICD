# test code by this command --> python -m pytest test_calculator.py
# pytest test_calculator.py

import pytest
# import sys
# import os
# sys.path.append(os.path.abspath(".."))
from calculator import add,divide

def test_add():
    # Assert -> Assertion(condition) => Output Result
    assert add(2,3) == 5
    
def test_add2():
    # Assert -> Assertion(condition) => Output Result
    # False Case
    assert add(2,3) == 4
    

def test_divide():
    assert divide(10, 2) == 5

def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(10, 0)
         
    
    
    
    
    
# Creating new Environment
# python -m venv venv
# venv\Scripts\activate - for poweshel and A or a
# pip install pytest
# pytest

# venv\Scripts\activate.bat - for CMD
# source venv/bin/activate - for Linux