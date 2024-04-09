#  Python Program to Merge Two Lists and Sort it

l1=[]
l2=[]
n1=int(input("Enter the no of elements in 1st list : "))

for i in range(n1):
    a=int(input("Enter the elements in 1st list : "))
    l1.append(a)

n2=int(input("Enter the no of elements in 2nd list :"))
for i in range(n2):
    a=int(input("Enter the elements in 2nd list: "))
    l2.append(a)

print("1st List is: ", l1)
print("2nd List is: ", l2)
l=l1+l2
print("Final Merge List is: ", l)
l.sort()
print("Sorted list is",l)