#Python Program to Determine Whether a Given Number is Even or Odd Recursively

def check(n):
    if n<2:
        return n % 2 == 0
    return (check(n-2))

n=int(input("Enter the number : "))
if (check(n)==True):
    print("This is an even number ")
else:
    print("This is an odd number ")

