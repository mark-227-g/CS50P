from project import validate_zipcode
from project import get_weather
from project import get_time
import pytest

def test_validate_zipcode():
    assert validate_zipcode("07028") is True
    assert validate_zipcode("07028-1234") is True
    assert validate_zipcode("070289") is False
    assert validate_zipcode("ABCDE") is False

def test_get_weather():
    try:
        get_weather("07030",1)
    except Exception as exc:
        assert False, f'Exception {exc}'
    try:
        get_weather("07030",2)
    except Exception as exc:
        assert False, f'Exception {exc}'

    with pytest.raises(Exception):
        get_weather("07030",0)
    with pytest.raises(Exception):
        get_weather("abcde",1)

def test_get_time():
    assert get_time("2023-01-13T18:00:00-05:00") == "18:00:00"
    assert get_time("2023-01-13T01:00:00-05:00") == "01:00:00"

