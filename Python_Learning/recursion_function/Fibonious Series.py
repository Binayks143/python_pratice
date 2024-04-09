def febo(num):
    if num==0:
        return num
    elif num==1:
        return num
    else:
        return febo(num-1)+febo(num-2)

num=int(input("Enter the number of terms: "))
print ("Fibonacci series")
if num<0:
    print ("Fibonacci series is not possible for -ve number")
else:
    for i in range (num+1):
        print(febo(i), end=' ')