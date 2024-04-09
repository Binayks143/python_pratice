# Python Program to Create a List of Tuples with the First Element as the Number and Second Element as the Square of the Number

l_limit=int(input("Enter the lower limt : "))
u_limit=int(input("Enter the Uper Limit : "))
l=[]
for i in range(l_limit,u_limit+1):
    a=(i,i**2)
    l.append(a)

print([l])

#or
#a=[(i,i**2) for x in range(l_limit,u_limit+1)]
#print(a)