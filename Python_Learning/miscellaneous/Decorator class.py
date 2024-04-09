def outer(func):
    print(func)
    print("Inside outer function")
    def inner():
        print("Inside inner function")
        oa=func()
        print(oa)
    return inner

print("Begin")
@outer
class A:
    print("Control Inside the class ")

A()
print("End")