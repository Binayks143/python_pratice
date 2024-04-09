#Python Program to Sort a List According to the Length of the Elements

l=[]
n=int(input("Enter the number of elements in lists : "))
for i in range(n):
    n1=input("Enter the elements :")
    l.append(n1)

print("Entered List is :",l)
l.sort(key=len)
print("Sorted List According to the Length of the Elements is :",l )