# USed to reduce the sequence of values into a single value
#reduce belongs to functool module so before using we have to import it

from functools import reduce
l=[2,5,6,8,4,7,5,2,66,99,100,4,1]

#1st way using function
def single(a,b):
    return a+b

red=reduce(single,l)
print(red)

# 2nd way using lambda function
red=reduce(lambda a,b:a+b,l)
print(red)