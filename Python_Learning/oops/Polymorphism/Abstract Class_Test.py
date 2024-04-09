from abc import ABC,abstractmethod

class A(ABC):
    @abstractmethod
    def disp(self):         #Can't instantiate abstract class
        pass

class B(A):
    pass                #Can't instantiate abstract because it is inheriating from class A so here it is compolsory to defind a method.


oa=B()
oa.disp()