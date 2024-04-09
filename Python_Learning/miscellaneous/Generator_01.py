#deifference between return and yield

def A():
    return 5
a=A()
print(a)

def B():
    yield 5
b=B()
print(b)        #we will get object of generator

def C():
    yield 1
    yield 2
    yield 3
    yield 4
c=C()
print(c)     #we will get object of generator
print(next(c))
#or
print(c.__next__())

#using loop
for i in c:
    print(i)