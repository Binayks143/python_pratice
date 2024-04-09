# Python Program to Create a Class and Get All Possible Subsets from a Set of Distinct Integers

class Subset:
    def f1(self,n):
        return self.f2([],sorted(n))

    def f2(self,temp,n):
        if n:
            return self.f2(temp,n[1:]) + self.f2(temp + [n[0]],n[1:])
        return [temp]

a=[]
n=int(input("Enter number of elements: "))
for i in range(0,n):
    a1=input("Enter the element:")
    a.append(a1)
print("input number are: ", a)
s1=Subset()
print("Subsets is", s1.f1(a))
