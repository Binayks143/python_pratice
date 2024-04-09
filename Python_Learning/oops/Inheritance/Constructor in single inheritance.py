#When constructor is defiend in parent class, the child class inherits the constructor of paren class

# class A:
#     a=10
#     b=20
#     def __init__(self):
#         print("Init in Parent class")
#
# class B(A):
#     c=30
#     d=40
# oa=A()
# ob=B()
# print(oa.a,oa.b)
# print(ob.a,ob.b,ob.c,ob.d)

#When constructor is defiend in both parent and
# child class then the objects of child and parents
# refer to respective class constructor.

class A:
    a=10
    b=20
    def __init__(self):
        print("Init in Parent class")

class B(A):
    c=30
    d=40
    def __init__(self):
        print('Init in child class')
oa=A()
ob=B()
print(oa.a,oa.b)
print(ob.a,ob.b,ob.c,ob.d)



