#Python Program to Exchange the Values of Two Numbers Without Using a Temporary Variable

a= int(input("Enter the 1st value :"))
b= int(input("enter the 2nd value :"))
print("before swaping")
print("Firt value is :" , a)
print("Second value is :", b)
print ("After swaping")

a=a+b
b=a-b
a=a-b


print("First value is: " ,a)
print("Second value is :", b)

