#wAP to add 5 elements in a list

a=[]
n=int(input('Enter the elemenmt to be added in a list:'))
for i in range(1,n+1):
    a1=int(input('Enter the elements:'))
    a.append(a1)
    print(a)

#using List Compreshion
lc=[x for x in range(1,n+1)]
print(lc)