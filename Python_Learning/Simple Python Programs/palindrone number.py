#Python Program to Check if a Number is a Palindrome
a=int(input("Enter a number: "))
temp=a
rev=0
while (a>0):
    b=a%10
    rev=rev*10+b
    a=a//10
print("Reverse number is: ", rev)
if temp==rev:
    print ("Number is a Palindrome")
else:
    print("Number is not Palindrome")
