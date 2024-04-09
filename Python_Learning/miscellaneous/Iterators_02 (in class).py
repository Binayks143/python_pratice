# previous e.g we have seen those are inbuild iterators, here will do how to create own iterator
#WAP to print top 10 number

class A:
    def __init__(self):
        self.num=1      #starting from 1
# for iteration 2 method are required 1) iter : which give object of iterator 2) next() : traverse
    def __iter__(self):
        return self

    def __next__(self):
        if self.num<=10:
            val=self.num
            self.num +=1
            return val
        else:
            raise StopIteration("Stop ieration")
            #used to stop iteration oterwise None will be printed

o1=A()
#1st way
print(o1.__next__())
print(o1.__next__())

#2nd way using loop
for i in o1:
    print(i)

#Note: in above 1st way case we already printed top 2 value so while prining in loop it will
#continiue from the last iteration (Once we get the value it will won't repeat)

