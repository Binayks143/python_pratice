#Python Program to Print all Numbers in a Range Divisible by a Given Number

a=int(input("Enter the lower limit"))
b=int(input("Enter the Upper limit"))
c=int(input("Enter the divident numer"))
'''res=list (range(a,b,5))
print (res)'''
for i in range (a,b+1):
    if (i%c==0):
        print (i)
