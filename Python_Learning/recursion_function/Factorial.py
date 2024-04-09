'''def fact(n):
    #n = int(input("Enter the number"))
    if n<=1:
        return 1

    else:
        return n * fact(n-1)

print(fact(5))'''

# using user input
def rec_fact(n):
    if n==1:
        return n
    else:
        return n* rec_fact(n-1)


n= int(input("Enter the number"))
if n<0:
    print ("Factorial does not exits")
else:
    print ("The Factorial of", n ,"is: " ,rec_fact(n))