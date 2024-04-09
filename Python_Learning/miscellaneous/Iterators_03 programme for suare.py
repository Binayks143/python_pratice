#wap to print series of nos with power of 2 from 0 to max

class A:
    def __init__(self,min,max):
        self.min=min
        self.max=max
    def __iter__(self):
        return self
    def __next__(self):
        if self.min<=self.max:
            result=self.min**2
            self.min+=1
            return result


max=int(input("Enter the maximun number: "))
oa=A(1,max)

for i in range(max):
    print(i+1,'power(2) is',oa.__next__())
# print(oa.__next__())
# print(oa.__next__())
# print(oa.__next__())

