#Fetch all the even no from a given list
#Filter will give boolean result if result is true thwn it will store the value

l=[2,5,6,8,4,7,5,2,66,99,100,4,1]
even1=[]
def even():
    for i in l:
        if i%2==0:
            even1.append(i)
    return even1
r=even()
print(r)

#Using filter func
def is_even(n):
    return n%2==0

even=list(filter(is_even,l))        #filter will take 2 arguments
print(even)

#Using Filter and lambda
even=list(filter(lambda n:n%2==0,l))        #if we are using fun only one time we can use lambda
print(even)

