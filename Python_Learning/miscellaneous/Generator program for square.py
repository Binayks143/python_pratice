class A:
    def __init__(self,min,max):
        self.min=min
        self.max=max
    def __iter__(self):
        return self
    def __next__(self):
        if self.min<=self.max:
            result=min**2
            min +=1
            yield result


max=print(int(input("ENter the maximum number: ")))
oa=A(1,max)

print(oa.__next__())
print(oa.__next__())
for i in range(max):
    print(next(i+1))
