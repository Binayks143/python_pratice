# Python Program to Find the LCM of Two Numbers Using Recursion
def lcm(n1,n2):
    if n1>n2:
        greater=n1
    else:
        greater=n2

    while(True):
        if ((greater%n1==0) and (greater%n2==0)):
            l=greater
            break
        greater=greater+1
    return l

n1=int(input('Enter first number: '))
n2=int(input('Enter Second number: '))
if (n1,n2 >0 ):
    print('Lcm of',n1,'&',n2, 'is :',lcm(n1,n2))
else:
    print('Invalid Input')
