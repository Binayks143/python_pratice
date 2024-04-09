
#FUnction inside a function is called nested func or inner functn

def Outer():
    print("Inside Outer function")
    def inner():
        print('Inside inner function')
        return "Returning to avoid NONE"
    return inner()

r=Outer()
print(r)
