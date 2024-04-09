# Python Program to Find the Binary Equivalent of a Number Recursively
l=[]
def convert(n):
    if n==0:
        return 1
    n1=n%2
    l.append(n1)
    convert(n//2)

n = int(input('Enter a decimal number: '))
if n>=0:
    convert (n)
    l.append(0)
else:
    convert((-n))
    l.append(1)
#print (l)
l.reverse()
#print(l)
print("The Binay number of", n ,'is', end=' ')
for i in l:
    print(i , end=' ')