import pytest
from working import convert

def test_invalid_minutes() :
    with pytest.raises(ValueError) :
        convert("9:60 AM to 5:60 PM")
def test_invalid_to():
    with pytest.raises(ValueError) :
        convert("9 AM - 5 PM")
def test_invalid_hour():
    with pytest.raises(ValueError) :
        convert("09:00 AM to 17:00 PM")
def test_missing_AM():
    with pytest.raises(ValueError) :
        convert("09:00 to 17:00 PM")
def test_bad_date():
    with pytest.raises(ValueError) :
        convert("10:30 PP to 8:50 AM")
    with pytest.raises(ValueError) :
        convert("10:30 PM to 8:50 FD")
    with pytest.raises(ValueError) :
        convert("14:30 PM to 8:50 AM")
    with pytest.raises(ValueError) :
        convert("10:30 PM to 30:50 AM")
    with pytest.raises(ValueError) :
        convert("10:90 PM to 8:50 AM")
    with pytest.raises(ValueError) :
        convert("10:30 PM to 8:90 AM")


def test_working() :
    assert(convert("9 AM to 5 PM"))=="09:00 to 17:00"
    assert(convert("9:00 AM to 5:00 PM"))=="09:00 to 17:00"
    assert(convert("10 PM to 8 AM"))=="22:00 to 08:00"
    assert(convert("10:30 PM to 8:50 AM"))=="22:30 to 08:50"
    assert(convert("12:00 AM to 12:00 AM"))=="00:00 to 00:00"
