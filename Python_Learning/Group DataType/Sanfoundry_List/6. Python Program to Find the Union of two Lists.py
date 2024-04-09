# Python Program to Find the Union of two Lists

l1=[]
l2=[]
n1=int(input("Enter the nos of element in first list : "))
for i in range(n1):
    n=input("Ener the elements: ")
    l1.append(n)

n2=int(input("Enter the nos of element in first list : "))
for i in range(n2):
    n=input("Ener the elements: ")
    l2.append(n)

print("1St list is : ",l1)
print("2nd list is : ",l2)

union=list(set().union(l1,l2))
intersection=list(set(l1) & set(l2))

print("Union of list l1 and l2 is : ",union)
print("Intersection of list l1 and l2 is : ",intersection)



