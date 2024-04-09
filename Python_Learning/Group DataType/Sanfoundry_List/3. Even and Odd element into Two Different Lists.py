#Python Program to Put Even and Odd elements in a List into Two Different Lists

l=[]
n=int(input("Enter number of element want to add in the list: "))
for i in range(n):
    a=int(input("Enter the element: "))
    l.append(a)
print("List is",l)
odd=[]
even=[]
for i in l:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
print("ODD list is",odd)
print("Even list is",even)
