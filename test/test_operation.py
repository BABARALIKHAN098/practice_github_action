from src.math import add, subtract
def test_add():
    assert add(2,2)==4
    assert add(3,5)==8

def test_subtract():
    assert subtract(5,2)==3
    assert subtract(10,3)==7