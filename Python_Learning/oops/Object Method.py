class Bank:
    bname='ICICI'               #Class (Static Variable)
    mname='Binay'               #Class (Static Variable)
    ifsc='ICICI454545'
    def __init__(self,cname,cphno,cmail=None):
        self.cname=cname        #Instance Variable
        self.cphno=cphno
        self.cmail=cmail

    def disp(self):
        print('Bank name is :',self.bname)
        print('Manager name is :',self.mname)
        print('IFSC code is :',self.ifsc)
        print('Customer name is :',self.cname)
        print('Customer phone number is :',self.cphno)
        print('Customer mail id is : ',self.cmail)

oa=Bank('Ram','7894584565','ram@gmail.com')
oa1=Bank('Raj',4545545454)
Bank.disp(oa)
print('----'*20)
Bank.disp(oa1)
#OR
print('===='*20)
oa.disp()
print('----'*20)
oa1.disp()