#Python Program to Find the Sum of Elements in a List Recursively
def sum1():
    e1=int(input("Enter the element : "))
    return e1

def sum2(l,n):
    if n==0:
        return 0
    else:
        return l[n-1]+sum2(l,n-1)


l=[]
n=int(input("Enter the no. of element is list : "))
for i in range(n):
    e1=sum1()
    l.append(e1)
    print(l)

print("Sum of the list elements is: ", sum2(l,n))