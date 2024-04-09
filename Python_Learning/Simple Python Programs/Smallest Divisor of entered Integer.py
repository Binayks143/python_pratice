#Python Program to Find the Smallest Divisor of an Integer

a=int(input("Enter the number : "))
b=[]
for i in range (2,a+1):
    if a%i==0:
        b.append(i)

b.sort()
print ("Smallest Divisor of entered Integer is : ", b[0])
    
