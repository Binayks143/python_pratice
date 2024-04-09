class A:
    def disp(self):
        print('Class A method')
class B(A):
#   pass                    # if disp() only in class A than ob=B() calls class A disp()
    def disp(self):         # if disp() is in class B than ob=B() override class A disp()
        print('Class B method')
ob=B()
ob.disp()
