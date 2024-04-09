#Python Program to Count the Number of Digits in a Number
a=int(input("Enter the number : "))
'''
l=[]
while (a>0):
    b=a%10
    l.append(b)
    a=a//10
print("Number of digit in entered number is: ", len(l))
'''
count=0
while (a>0):
    count=count+1
    a=a//10
print("Number of digit in entered number is: ",count)

    
