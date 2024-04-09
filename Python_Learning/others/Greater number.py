a=155
b=56000
c=566
d=984

if a>b:
    if a>c:
        if a>d:
            print ("a is greater")
        else:
            print ("d is greater")
        if c>d:
            print ("C is greater")
        else:
            print ("d is greater")
    elif b>c:
        if b>d:
            print ("b is greater")
        else:
            print ("d is greater")
            
    elif c>d:
        print ("c is greater")
else:
    print ("d is greater")
