a=[1,2,3,6,5,8,9,10]
for i in a:
    if i==5:
        continue
    print(i)
print("\n")

for i in range(1,10,1):
    if i in (6,7,8):
        continue
    print(i)

print("\n")
for i in range (1,10+1,1):
    print(i ,end=' ')


print("\n")
for i in range (10,0,-1):
    print(i, end=' ')
    
