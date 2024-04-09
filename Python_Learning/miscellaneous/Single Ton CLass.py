#STC which create only one object in its lifetime
def outer(cls):
    instances={}
    def inner():
        print("Dictionary data is", instances)
        if 'a' not in instances:
            instances['a']=cls()
        return instances
    return inner
@outer
class A:
    print("Contorl inside the class")