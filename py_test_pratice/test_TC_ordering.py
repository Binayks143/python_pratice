# By defult python execute the code or methods from top to buttom
# to run in specific order we have to install following packages
# pip3 install pytest-ordering

#########
#  http://pytest-ordering.readthedocs.io/en/develop/
########

import pytest
@pytest.mark.run(order=2)
def test_order_methodA(OneTimeCall,setUp):
    print("Running Method A")

@pytest.mark.run(order=3)
def test_order_methodB(OneTimeCall,setUp):
    print("Running Method B")

@pytest.mark.run(order=1)
def test_order_methodC(OneTimeCall,setUp):
    print("Running Method C")

@pytest.mark.run(order=5)
def test_order_methodD(OneTimeCall,setUp):
    print("Running Method D")

@pytest.mark.run(order=4)
def test_order_methodE(OneTimeCall,setUp):
    print("Running Method E")

#Output should be : C A B E D



