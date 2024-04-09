from abc import ABC,abstractmethod

class Polygon(ABC):
    @abstractmethod
    def sides(self):                #Abstract Method
        pass

class Traingle(Polygon):
    def sides(self):                #Override Abstract Method
        print("Traingle has 3 sides")

class Pentagon(Polygon):
    def sides(self):                #Override Abstract method
        print("Pentagon has 5 sides")

class Circle(Polygon):
 #   def disp(self):            # here it is compulsory to have sides()
        #print("It has no sides")
    def sides(self):
        print("It has no sides")

T1=Traingle()
T1.sides()
P1=Pentagon()
P1.sides()
C1=Circle()
C1.sides()