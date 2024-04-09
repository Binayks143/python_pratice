#used to compair and raise the exception error name
#it trace the exception if the condition false
#e.g.
#assert 10>11,'10 is not greater then 11'

def add(a,b):
    return a+b
assert 30==add(10,20),'Not same'        #true so no exception
assert 30==add(20,40),'Not Same'        #False so AssertionError: Not Same

