import math
class Circle:
    def __init__(self,n):
        self.n=n
    def area(self):
        area=math.pi*self.n**2
        return area
    def perimeter(self):
        p=2*math.pi*self.n
        return p

n=int(input("Enter the radius of circle: "))
c1=Circle(n)
print("Area of circle is:",round(c1.area(),3))
print("Perimeter of circle is :",round(c1.perimeter(),3))


