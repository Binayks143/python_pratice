from SpecialVariableName_4 import sum
def func1():
    print ("From func1")
    sum()

def func2():
    print ("From func2")

def main(): #Standard function it not calling it self. from here we will call all other function
    func1()
    func2()

main()

