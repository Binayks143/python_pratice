#used to substitute the matched patterns
import re

#sub()
data='Hi all how are you learning python?'
a=re.sub(r'\w{2}',"$",data)     #replces first two letter of each word with $ in a sentance
print(a)

ph='9857458569'
b=re.sub(r'\w{7}',"*******",ph)     #Replaced first 7 number with *
print(b)

a=re.sub(r'\w{3}',"#",data,5)   #replaced data sentance words with # upto 5 word
print(a)

a=re.sub(r'^\w','$',data)       #replaces only 1st char of sentance
print(a)

#subn()
a=re.subn(r'\w{2}',"@",data)    #Same as above but returned the output in the form of tuple
print(a)

#split()
a=re.split(r'\s',data)
print(a)