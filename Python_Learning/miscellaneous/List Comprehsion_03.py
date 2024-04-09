# Square of all odd numbers from range 1 to 10
print([x ** 2 for x in range(1,10+1) if x%2==1])

#list contains power of 2 from 1 to 8
print([2**x for x in range(1,8+1)])

# list contains prime and non-prime in range 1 to 50
#prime=[x for x in range(1,51) if x%2]

#lowering the characters
print([x.lower() for x in ['A','B','C','D']])

# list which extracts number from below string
s='Hi may name is binay and my phone number is 988756456546'
print([x for x in s if x.isdigit()])
