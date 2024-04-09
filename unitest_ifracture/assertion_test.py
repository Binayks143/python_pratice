#Asser method is used to find wheater a test case is pass or failed
'''
for more info visit the following page
https://docs.python.org/3/library/unittest.html#unittest.TestCase
'''
# When assert testcase failed it will not go the next line but will go to next method

import unittest

class Demo_Assert(unittest.TestCase):
    def test_assertTrueFalse(self):
        a=True
        b=False
        self.assertTrue(a,"a is not true")
        self.assertFalse(b,'b is not false')

    def test_assertEqual(self):
        a='Binay'
        b='Binay'
        self.assertEqual(a,b,msg="A is not equal to B")
        #self.assertNotEqual(a,b,msg="A is equal to B")


if __name__=="__main__":
    unittest.main(verbosity=2)
