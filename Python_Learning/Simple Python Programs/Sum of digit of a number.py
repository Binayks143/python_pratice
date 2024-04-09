#Python Program to Find the Sum of Digits in a Number
a=int(input("Enter the number : "))
print("Enter number is ", a)
tot=0
while a>0:
    b=a%10
    tot=tot+b
    a=a//10
print("Sum of digit is : ", tot)
        
    
