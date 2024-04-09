import unittest         # unit testing framework

class TestCaseDemo1(unittest.TestCase):
    def setUp(self) -> None:
        print("I will run brfore every test case")
    def test_methodA(self):
        print("Running methodA")
    def test_methodB(self):
        print("Running methodB")
    def test_methodC(self):
        print("Running methodC")

    def tearDown(self) -> None:
        print("I will run after every test case")

if __name__=='__main__':
    unittest.main(verbosity=2)
