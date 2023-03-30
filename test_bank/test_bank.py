from bank import value

def test_value_hello():
    assert value("hello")==0
    assert value("HELLO")==0
    assert value("Hello")==0

def test_value_h():
    assert value("hippo")==20
    assert value("HIPPO")==20
    assert value("Hippo")==20

def test_value_not_hello():
    assert value("wrong")==100
    assert value("WRONG")==100
    assert value("Wrong")==100