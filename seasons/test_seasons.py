import pytest
import datetime
from seasons import number_minutes_from_today, format_number_words

def test_number_word():

    assert number_minutes_from_today(datetime.datetime(2022, 11, 17))==1440
    assert number_minutes_from_today(datetime.datetime(2022, 11, 16))==2880

def test_minutes():
    assert format_number_words(100)=="One hundred"
    assert format_number_words(1440)=="One thousand, four hundred forty"
