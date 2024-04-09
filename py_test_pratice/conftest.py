'''
import pytest

@pytest.yield_fixture()
def setUp():
    print("Running Method level setUp")
    yield
    print("Running Method level tearDown")

@pytest.yield_fixture(scope="module")
def OneTimeCall():
    print("Running one time setUp")
    yield
    print("Running one time tearDown")
'''

# Command line arguments changes
import pytest

@pytest.yield_fixture()
def setUp():
    print("Running Method level setUp")
    yield
    print("Running Method level tearDown")

@pytest.yield_fixture(scope="module")
def OneTimeCall(osType,browser):
    print("Running one time setUp")

    if osType=='window':
        print("Running in window system")
        if browser =='firefox':
            print("Running tests in firefox")
        else:
            print("Running test in Chrome")
    else:
        print("Running in Mac system")
        if browser =='firefox':
            print("Running tests in firefox")
        else:
            print("Running test in Chrome")
    yield
    print("Running one time tearDown")

def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--osType",help="Type of OS")  #help is used to help user the user of --os

@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture(scope="session")
def osType(request):
    return request.config.getoption("--osType")

