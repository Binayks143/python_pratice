import time
def outer(func):
    def wrapper(a):
        start = time.time()
        func(a)
        end = time.time()
        time1=str((end-start)*1000)
        print("Time taken for " + func.__name__ + " is " + time1 +" Milli second")
    return wrapper

@outer
def square(n):
    result=[]
    for i in n:
        result.append(i*i)
    return result

@outer
def cube(n):
    result=[]
    for i in n:
        result.append(i*i*i)
    return result

p=range(1,50000)
q=square(p)
c=cube(p)
#print(c)
