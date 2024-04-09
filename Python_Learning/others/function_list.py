def dynlist ():
    a=[]
    n= int(input("ENTER THE NOS. OF LIST ELEMENTS TO BE ADDED"))

    for i in range (n):
        element=input("enter the elements")
        a.append(element)
        print(a)

dynlist()
