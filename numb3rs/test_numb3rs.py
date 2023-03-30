from numb3rs import validate

def test_validate():
    assert validate("1.1.1.1")==True
    assert validate("10.10.10.10")==True
    assert validate("100.100.100.100")==True
    assert validate("255.1.1.1")==True
    assert validate("1.255.1.1")==True
    assert validate("1.1.255.1")==True
    assert validate("1.1.1.255")==True
    assert validate("255.255.255.255")==True

#def test_validate_False():
    assert validate("256.1.1.1")==False
    assert validate("1.256.1.1")==False
    assert validate("1.1.256.1")==False
    assert validate("1.1.1.256")==False
    assert validate("255.255.255.256")==False
    assert validate("a.1.1.1")==False
    assert validate("1.1.1")==False

