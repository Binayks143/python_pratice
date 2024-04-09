# Python Program to Find if a Number is Prime or Not Prime Using Recursion

def check(n,div=None):
    if div is None:
        div=n-1
        while (div>=2):
            if n % div==0:
                print("This is not a prime number ")
            else:
                return check(n,div-1)
    else:
        print("This is Prime number ")
        return True


n=int(input('Enter the number: '))
check(n)