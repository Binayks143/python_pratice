#Python Program to Find the Second Largest Number in a List

l=[]
n=int(input("Enter number of element want to add in the list: "))
for i in range(n):
    a=int(input("Enter the element: "))
    l.append(a)
print("List is",l)
l.sort()
print("Second Largest Number in a List is :",l[-2])