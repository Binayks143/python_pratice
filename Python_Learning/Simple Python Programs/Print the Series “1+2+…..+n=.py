#Python Program to Read a Number n And Print the Series “1+2+…..+n= “
a=int(input("Enter the last number : "))
l=[]
for i in range(1,a+1):
    print (i,end= " ")
    if (i<a):
        print(" + ",end='')
    l.append(i)

print("=" , sum(l))
