#Public : The members declared as Public are accessible from outside the Class through an object of the class.
#Protected: The members declared as Protected are accessible from outside the class but only in a class derived from it that is in the child or subclass.
#Private: These members are only accessible from within the class. No outside Access is allowed.

class Bank():
    def __init__(self,bname,ifsc,credit):       #constructor
        self.bname=bname                        #public variable
        self._ifsc=ifsc                         #Protected
        self.__credit=credit                    #Private

    def credit(self):
        print("Bank credit is:",self.__credit)

class customer(Bank):                           #chile class of bank
    def __init__(self,bname,ifsc,cname,cphno,sal,credit):
        self.cname=cname
        self.cphno=cphno
        self.__sal=sal                  #private
        super().__init__(bname,ifsc,credit)       #calling parent class contructor

    def disp(self):
        print('Bank name is:',self.bname,'\nBank IFSC code is:',self._ifsc,'\nCustomer name is:',self.cname,'\nCustomer Ph no is:',self.cphno,'\nSalary is',self.__sal)

        #print("Bank Credit is:",self.__credit)    #This is private member of class A can't inherate

c1=customer('HDFC','HDFC12540','RAM',545454545,120000,50000000)
c1.disp()
#print(c1.__sal) we cant call private member outside the class
print(c1._customer__sal)    # with _class__var we can access the provate member outside the class

b1=Bank('HDFC','HDFC12540',5454545400)
#print(b1.__credit)          # private memer of bank can't called AttributeError:
print("Bank credit is :", b1._Bank__credit)     #like this we can called private member

b1.credit()     #private member of that class can access private variable