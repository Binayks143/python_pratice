class A:
    def __init__(self,a,b,c):
        self.a=a
        self._b=b
        self.__c=c

    def disp(self):

        print('Value of a is : ',self.a)
        print('Value of b is : ',self._b)
        print('Value of c is : ',self.__c)

class B(A):
    def disp(self):
        print('Value of a is :',self.a)
        print('Value of b is :',self._b)
       # print('Value of b is :',self.__c)       AttributeError: 'B' object has no attribute '_B__c'
        print('value of c is :', self._A__c)    # Private in class A


oa=A(1,2,3)
oa.disp()

ob=B(5,6,7)
ob.disp()
