# in the previous programme (Method_overloading_01) we have seen method overloading a
# chived my assigning default value to args in this programme we will perform method
# overloading using generic arguments i.e. none
#min mandatory value =2,  max ars =5, data type = any

# def add(a,b,c=None,d=None,e=None):
#     return a+b+c+d+e
# print(add(8787,99))
# o/p: error unsupported operand type(s) for +: 'int' and 'NoneType'

def add(a,b,c=None,d=None,e=None):
    if c==None and d== None and e== None:
        return a+b
    elif d==None and e== None:
        return a+b+c
    elif e==None:
        return a+b+c+d
    else:
        return a+b+c+d+e

print(add(45,88))
print(add(45,88,565.56))
print(add('hello','Hi'))
print(add([1,2,3],[4,5,6]))
print(add([1,2,3],[4,5,6],[8],[23.450,[78]]))




