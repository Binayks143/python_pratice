#Python Program to Print Odd Numbers Within a Given Range

a=int(input("Ente the lower range"))
b=int(input("Ente the upper range"))
'''if (a%2 !=0):
    print (list(range(a,b,2)))
else:
    a=a+1
    print (list(range(a,b,2)))'''
for i in range(a,b+1):
    if (i%2 !=0):
        print(i)
