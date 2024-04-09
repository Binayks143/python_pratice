def dyn():
    a=[]
    n=int(input("enter the no of list element to be added : "))
    for i in range (n):
        option=input("enter the type of element you want to add : ")
        if option=='int':
            x=intfunc()
            a.append(x)
            print(a)
            
def intfunc():
    i=int(input("Enter the interger value"))
    return i

dyn()
