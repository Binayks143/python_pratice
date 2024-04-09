class A:
    def disp(self):
        print('CLass a value')

class B:
    def disp(self):
        print('B class value')

class C:
    oa=A()
    def disp(self):
        print('class c value')

c1=C()
c1.oa.disp()
c1.disp()
#c1.d(id)