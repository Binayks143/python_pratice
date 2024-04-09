#Python Program to Find the Largest Number in a List
l=[]
n=int(input("Enter number of element want to add in the list: "))
for i in range(n):
    a=int(input("Enter the element: "))
    l.append(a)
print("List is",l)

print("The Largest number is", max(l))
#2nd way
l.sort()
print("The Largest number is",l[-1])

