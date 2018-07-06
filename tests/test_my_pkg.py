'''Tests the mathmatical functions defined in my_pkg/trial.py and demo/trial.py (I think)
'''
import pytest
def test_square():
'''Tests the squaring function
'''
  from my_pkg.trial import square
  from demo.trial import square
  assert 4 == square(2)
