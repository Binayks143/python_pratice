#Find the even number

# (1) Using For loop
a=[]
n=[1,4,5,9,6,7,8]
for i in n:
    if i%2==0:
        a.append(i)
print(a)

#using List Comprehsion
lc=[x for x in n if x%2==0 ]
print(lc)