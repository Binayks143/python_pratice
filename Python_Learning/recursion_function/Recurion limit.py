def rec(n):
    print(n)
    #rec(n-1)
rec(5)

import sys
print(sys.getrecursionlimit())
sys.setrecursionlimit(2000)
print(sys.getrecursionlimit())



