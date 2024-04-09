def sum():
    print ("Addition",__name__)     #same module its became __main__

def sub():
    print ("Substraction")

def mul():
    print ("multiplication")

def main():
    print("From SpecialVariableName_4")
    sum()
    sub()
    mul()
if __name__ =="__main__":      # IT will use only for current module because here __name__== __main__
    main()