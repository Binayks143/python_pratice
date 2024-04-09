l=["l","d","dg","45.56"]
print(l)
for i in l:
    print([i],end="")
print(l[2])
l1=l
print("l1=", l1)
l1[2]="kooo"
print("l1=", l1)
length=len(l1)
print(length)
l1.append("bbb")
length=len(l1)
print(length)
print(l1)
l1.insert(2,"test")
length=len(l1)
print(length)
print(l1)

x=l1.index("test")
print(x)
l1.pop()
print(l1)

l1.remove("d")
print(l1)

slicing=l1[1:3]
print(slicing)

l1.sort()
print(l1)

print(len(l1))
print(l1.count('l'))

print("*"*50)
#Dictionaries.

dict={'cars':'BMW','Bike':'Honda','Auto':'Bajaj'}
print(dict)
print(dict['cars','Bike'])