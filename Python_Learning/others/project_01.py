def dynlist():
    a=[]
    n= int(input("Enter the no. elements to be added in list : "))
    for i in range (n):
        option=input("Enter the type of element :  ")
        if option =='int':
            element =intfunc()
            a.append(element)
            print (a)
        elif option == 'float':
            element =floatfunc()
            a.append(element)
            print (a)
        elif option == 'bool':
            element = boolfunc()
            a.append (element)
            print (a)
        elif option == 'list':
            element = listfunc()
            a.append (element)
            '''elif option == 'tuple':
            element = tuplefunc()
            a.append (element) '''
        elif option == 'set':
            element = setfunc()
            a.append (element)
            print (a)
        elif option == 'dict':
            element = dictfunc()
            a.append (element)
            print (a)
        else:
            element =str (input(("Enter the elements in list : ")))
            a.append(element)
            print (a)

def intfunc():
    element=int(input("Enter the element :  "))
    return element

def floatfunc():
    element = float(input("Enter the element : "))
    return element

def boolfunc():
    element = bool (input("Enter the element : "))
    return element

def listfunc():
    temp=[]
    n = int (input ("enter the no. of elements of list : "))
    for i in range(n):
        element = str (input ("Enter the element in list : "))
        temp.append(element)
    print (temp)
    return temp

'''
def tuplefunc():
    temp=()
    n = int (input ("enter the no. of elements of tuple : "))
    for i in range(n):
        element = str (input ("Enter the element in tuple"))
        temp.append(element)
    print (temp)
    return temp'''

def setfunc():
    temp=set ()
    n = int (input ("enter the no. of elements of set : "))
    for i in range(n):
        element = str (input ("Enter the element in set : "))
        temp.add (element)
    print (temp)
    return temp


def dictfunc():
    temp={}
    n = int (input ("enter the no. of elements of Dictionary : "))
    for i in range(n):
        key = input ("Enter the key element : ")
        value =input ("Enter the value : ")
        temp[key]=value
    print (temp)
    return temp


dynlist()


        


