class A:
    a=10
    def disp(self):
        print('DIsp in class A')

class B(A):
    b=20
    def disp(self):
        print('Disp in class B')
    oa=A()

ob=B()
ob.disp()
ob.oa.disp()
