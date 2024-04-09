#this fun is used to convert the non string data to string data
#in User defiend exception_03 whe were getting type error exception
#in this program using repr() we will solve previous problem

class a(Exception):
    def __init__(self,msg):
        self.msg=msg
    def __str__(self):
        return repr(self.msg)
try:
    if 10==10:
        raise a(10)
except a as e:
    print(e)