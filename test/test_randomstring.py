import pytest, sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../src/')

from randomizer import getRandomString

def test_RandomizeString():
    result1 = getRandomString(13)
    result2 = getRandomString(13)
    assert result1 != result2
    assert 13 == len(result1)
    assert len(result1) == len(result2)
