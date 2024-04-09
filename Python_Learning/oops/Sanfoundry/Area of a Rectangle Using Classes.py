class rectangle:
    def __init__(self,len,bre):
        self.len=len
        self.bre=bre
    def area(self):
        result=self.len*self.bre
        return result



a=int(input('ENter the length of rectangle: '))
b=int(input('ENter the Breadth of rectangle: '))
r1=rectangle(a,b)
a1=r1.area()

print("Area of rectangle is :", a1)