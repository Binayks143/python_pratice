def outer(func):
    print(func)
    print('Inside outer func')
    def inner():
        print('Inside inner function')
        func()
    return inner

print("Began")
@outer
def display():
    print('Inside display')

display()
print('End')
