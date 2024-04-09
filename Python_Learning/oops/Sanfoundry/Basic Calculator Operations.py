#Python Program to Create a Class which Performs Basic Calculator Operations

class Cal:
    def __init__(self,n1,n2):
        self.n1=n1
        self.n2=n2
    def add(self):
        add=self.n1+self.n2
        return add
    def sub(self):
        if self.n1>self.n2:
            sub=self.n1-self.n2
        else:
            sub=self.n2-self.n1
        return sub
    def mul(self):
        m1=self.n1*self.n2
        return m1
    def div(self):
        d1=self.n1//self.n2
        return d1

print("Select the any number to perform operation\n1: Addition\t2: Substraction\t3: Multiplication\t4: Division")
n=int(input("Select the operation: "))
a1=int(input("Enter the 1st number:"))
a2=int(input("Enter the 2nd number:"))
c1 = Cal(a1,a2)
if n==1:
    print("Summation of",a1,'&',a2,'is',c1.add())
elif n==2:
    print("Substraction of",a1,'&',a2,'is',c1.sub())
elif n==3:
    print("Multiplication of",a1,'&',a2,'is',c1.mul())
elif n==4:
    print("Division of",a1,'&',a2,'is',c1.div())
else:
    print("Invalid input")


