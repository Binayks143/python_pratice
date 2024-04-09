import unittest
from unitest_ifracture.test_case_demo_01 import TestCaseDemo1
from unitest_ifracture.test_case_demo_02 import TestCaseDemo2

# Get all tests from both files TestCaseDemo1 & TestCaseDemo2

tc1=unittest.TestLoader().loadTestsFromTestCase(TestCaseDemo1)
tc2=unittest.TestLoader().loadTestsFromTestCase(TestCaseDemo2)

# Create a test suite combining TestCaseDemo1 & TestCaseDemo2

smoke_test=unittest.TestSuite([tc1,tc2])

#Running the test suite

unittest.TextTestRunner(verbosity=2).run(smoke_test)