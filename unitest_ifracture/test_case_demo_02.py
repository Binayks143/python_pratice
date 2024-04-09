import unittest

class TestCaseDemo2(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print("#"*60)
        print("I will run brfore ALL test case AT ONCE")
        print("#"*60)

    def test_methodA(self):
        print("Running methodA")
    def test_methodB(self):
        print("Running methodB")
    def test_methodC(self):
        print("Running methodC")

    @classmethod
    def tearDownClass(cls) -> None:
        print("*"*60)
        print("I will run after ALL test case AT ONCE")
        print("*"*60)

if __name__=='__main__':
    unittest.main(verbosity=2)