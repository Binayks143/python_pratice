#general way
def square(n):
    return n*n
print(square(5))

#Using Lambda
l=lambda n:n*n
print(l(6))

#Using more then one variable
l=lambda a,b:a+b        #here we have give only one exprression
r=l(55,5)
print(r)
