import pytest

@pytest.yield_fixture()
def fun1():
    print("Run before, every test cases")
    yield           #Optioal
    print("Run after every test cases")

def test_fixture2_method1(fun1):         #calling fixture here
    print("Running method 1")
@pytest.mark.skip
def test_fixture_method2(fun1):
    print("Running method 2")

@pytest.mark.xfail
def test_fixture_method3():
    print("How r u?")