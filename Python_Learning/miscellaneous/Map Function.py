#Map will take the no. of data and performed some action on it

l=[2,5,6,8,4,7,5,2,66,99,100,4,1]

# 1st way
def update(n):
    return n**2

value=list(map(update,l))
print(value)

# 2nd Way using lambda
value=list(map(lambda n:n**2,l))
print(value)
