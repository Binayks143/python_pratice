#Python Program to Read a Number n and Compute n+nn+nnn

num=int(input("Enter the number n :"))
t1=str(num)
t2=t1+t1
t3=t1+t1+t1

s=int(t1)+int(t2)+int(t3)
print("n+nn+nnn =",t1,'+',t2,'+',t3)
print("Sum is",s)
