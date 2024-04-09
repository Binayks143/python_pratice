# Python Program to Find the Sum of the Digits of the Number Recursively
l=[]
def digit(n):
    if n==0:
        return 1
    n1=n%10
    l.append(n1)
    digit(n//10)

n=int(input('Enter a number: '))
digit(n)
#print (l)
print('Sum of the digits of number ',n,'is', sum(l))