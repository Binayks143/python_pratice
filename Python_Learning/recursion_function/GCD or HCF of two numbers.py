def hcf(n1,n2):
    if n1>n2:
        smaller=n2
    else:
        smaller=n1
    for i in range(1,smaller+1):
        if ((n1%i==0) and (n2%i==0)):
            result=i
    return result

n1=int(input('ENter the 1st number: '))
n2=int(input('ENter the 2nd number: '))

print('Hcf of', n1,'and', n2,'is ', hcf(n1,n2))