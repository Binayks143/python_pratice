#unpacking : Extracting the elements from group data items and storing in individual variable
#max variable=6, mandatory=3 type =any

ab=[1,2,3,4,5,6]      #grpouped element
ab1=(54,'lisy',545)

def unpacking(a,b,c,d=None,e=None,f=None):
    print(a)
    print(b)
    print(c)
    print(d)
    print(e)
    print(f)

unpacking(*ab)
unpacking(*ab1)

