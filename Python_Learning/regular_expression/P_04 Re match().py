import re
data='This is inform that the information is informed to all'
b=re.match(r'(.*)',data)
print(b)
#print(dir(b))
c=re.match(r'(.*) (.*) (.*) (.*)',data)
print(c)
print(c.group(0))
print(c.group(1))
print(c.group(2))
print(c.group(3))
print(c.group(4))
#print(c.group(5))  #No such group
