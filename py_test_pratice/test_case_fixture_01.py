import pytest

@pytest.fixture()
def setUp():
    print("Run before, every test cases")

def test_fixture1_method1(setUp):         #calling fixture here
    print("Running method 1")

def test_fixture2_method2():
    print("Running method 2")