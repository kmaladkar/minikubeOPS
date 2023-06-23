import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from src.ops import *

def test_add():
    assert add(2,3) == 5

def test_subtract():
    assert subtract(2, 3) == -1

def test_multiply():
    assert multiply(2, 3) == 6

def test_divide():
    assert divide(10,5) == 2

##########
## Test
##########
####