"""
file name should start or end with test
test method name should start with test

py.test test_mod.py   # run tests in module
py.test somepath      # run all tests below somepath
py.test test_module.py::test_method  # only run test_method in test_module

-s to print statements
-v verbose
"""
import pytest

@pytest.yield_fixture()
def fun1():
    print("Run before, every test cases")
    yield           #Optioal
    print("Run after every test cases")

def test_running_method1(fun1):         #calling fixture here
    print("Running method 1")

def test_running_method2(fun1):
    print("Running method 2")

# py.test test_running_text_cases.py -v  ---> to run all method from this file
# py.test test_running_text_cases.py::test_running_method2 -v  ----> to run the specific method under a python file
