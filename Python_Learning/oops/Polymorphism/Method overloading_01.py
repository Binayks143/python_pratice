# Data type is not considered but rather then number of arguments will be considered

#Dynamic type or variable nos of args methos overloading achived

#In below e.g. nos of argument is fixed i.e. 2
print("No. of args are Fixed i.e. 2 ")
class A:
    def add (a,b):
        return a+b
oa=A()

print(A.add(4,5))
print(A.add(4.5,5.51))
print(A.add('abc','def'))
print(A.add([1,2,3],[4,5,6,3]))


# How to achived where no. of args are variable
# here three req should be available
# (1) Min mandatory args        (2) Max no of args that a method can have       (3) data type
# E.g.1 ->(1) Min mandatory args=2   (2) Max no of args that a method can have = 5  (3) data typ =int

print("\nHow to achived where no. of args are variable data type int/float")
def add(a,b,c=0,d=0,e=0):
    return a+b+c+d+e
print(add(5,45))
print(add(5,45,99))
print(add(5,45,99,887))
print(add(5,45,99,887,8))           # int
print(add(5,45,99.12,887.55))       # float

print("\nHow to achived where no. of args are variable here data type= str")

def str(a,b,c='',d='',e=''):
    return a+b+c+d+e
print(str('apple','orange'))
print(str('app','bpp','cpp'))
print(str('app','bpp','cpp','rpp'))
print(str('app','bpp','cpp','rpp','lpp'))

print("\nHow to achived where no. of args are variable here data type= list")

def lst(a,b,c=[],d=[],e=[]):
    return a+b+c+d+e
print(lst([44,58,55],[1,2]))
print(lst([44,58,55],[1,2],[5]))
print(lst([44,58,55],[1,2],[5],[6.555]))
print(lst([44,58,55],[1,2],[5],[6.555],[0]))










