a=int(input('enter the number of element in list : '))
l=[]
for i in range(a):
    b=int(input("enter the elements in list :"))
    l.append(b)
    print("The list is", l)
    
print("sum of list elements is= ",sum(l))
avg=sum(l)/a
print("Average of list element is= ", round(avg))
    
