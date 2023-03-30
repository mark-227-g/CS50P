import pytest
from um import count

def test_count():
    assert(count("hello, um, world"))==1
    assert(count("this is Um, what um it is"))==2
    assert(count("the umpire is um, out"))==1
    assert(count("UM, what's um up doc...um:"))==3
    assert(count("yummy"))==0
    assert(count("curriculum"))==0
    assert(count("ILLUMINATE"))==0
    assert(count("umpire"))==0
    assert(count("museum"))==0