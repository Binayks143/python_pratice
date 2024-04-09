#Python Program to Accept Three Digits and Print all Possible Combinations from the Digits

n1=int(input("Enter the 1st number"))
n2=int(input("Enter the 2nd number"))
n3=int(input("Enter the 3rd number"))
d=[]
d.append(n1)
d.append(n2)
d.append(n3)

print("Enter digits are :", d)
for i in range(0,3):
    for j in range (0,3):
        for k in range (0,3):
            if (i!=j & j!=k & k!=i):
                print(d[i],d[j],d[k])
