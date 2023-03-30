from fuel import convert, gauge
import pytest

def test_convert():
    assert convert("3/4")==75
    assert convert("1/2")==50
    assert convert("4/7")==57
    with pytest.raises(ValueError):
        convert("3/2")
    with pytest.raises(ZeroDivisionError):
        convert("1/0")
    with pytest.raises(ValueError):
        convert("A/B")

def test_gauge():
    assert gauge(0)=="E"
    assert gauge(1)=="E"
    assert gauge(100)=="F"
    assert gauge(99)=="F"
    assert gauge(75)=="75%"
