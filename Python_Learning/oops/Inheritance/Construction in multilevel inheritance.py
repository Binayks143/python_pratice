# When constructor is defiend only in parent class, the object of child and sub child class refer to parent class contruction.
print('Construction only in parent class')
class A:
    a=10
    def __init__(self):
        print('Init in Class A')

class B(A):
    b=20

class C(B):
   pass

oa=A()
ob=B()
oc=C()


# When constructor is defiend in all the class it refers to its respective constructor.
print("\nConstruction is in all classes")
class A1:
    def __init__(self):
        print('Init in class A')

class B1(A1):
    def __init__(self):
        print('Init in class B')

class C1(B1):
    def __init__(self):
        print('Init in class C')

oa1=A1()
ob1=B1()
oc1=C1()