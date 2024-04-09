class A:
    a=10
    b=20
    def __init__(self,x):
        self.x=x
        print('Init in parent class')
        print("X=",self.x)

class B(A):
    c=30
    d=40
    def __init__(self,x,y):
        self.y=y
        print('Init in Child class')
        print("Y=",self.y)
        super().__init__(x)
        #or
        A.__init__(self,x)

ob=B(12,15)
