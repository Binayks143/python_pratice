def topten():
    n=1
    while n<=10:
        yield n
        n +=1

n=topten()
print(n)
for i in n:
    print(i)