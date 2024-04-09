# Programme to compair the age of two student:

class student:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def disp(self):
        print('Name of the student is',self.name, '&', 'age is',self.age)

    def compair(self,other):
        if self.age==other.age:
            return True
        else:
            return False

s1=student('Raj',25)
s2=student('Babu',28)
s1.disp()
s2.disp()
if s1.compair(s2):
    print("The age is same")
else:
    print("Age is different")
