
class a(Exception):
    def __init__(self,msg):
        self.msg=msg
        print(self.msg)
    def __str__(self):
        return self.msg
try:
    if 10==10:
        raise a('10')       # raise a string type
except a as e:
    print(e)


class a(Exception):
    def __init__(self, msg):
        self.msg = msg
        print(self.msg)

    def __str__(self):
        return self.msg     #__str__ should return only string type
try:
    if 10 == 10:
        raise a(10)  # raise a interger type
except a as e:
    print(e)

