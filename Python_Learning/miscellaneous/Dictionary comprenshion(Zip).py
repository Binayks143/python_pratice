#Dict= {Key:Value for(Key,Value) in iterable}
#Zip : it is use to mapped the similar index of multiple containers.

name=['Raj','Binod','Ajay','Ram','Vivek']
designation=['Engineer','Doctor','Businessman','Builder','Software engg']

print(name,designation)
a=zip(name,designation)
print(a)
b=[zip(name,designation)]
print(b)

#method-1
l=list(zip(name,designation))
print(l)

#method-2
print({key:value for(key,value) in  zip(name,designation)})

#method -3

def dc(key,value):
    return {key[i]:value[i] for i in range (len(key))}

a=dc(name,designation)
print(a)