class Bank:
    bname='ICICI'
    mname='Binay'
    ifsc='ICICI454545'
    def __init__(self,cname,cphno,cmail=None):
        self.cname=cname
        self.cphno=cphno
        self.cmail=cmail

    def disp(self):                                 #instance method
        print('Customer details is ')
        print('Bank name is :',self.bname)
        print('Manager name is :',self.mname)
        print('IFSC code is :',self.ifsc)
        print('Customer name is :',self.cname)
        print('Customer phone number is :',self.cphno)
        print('Customer mail id is : ',self.cmail)
    def modify(self):                              #instance method
        print('\nPress the number to modify the above details: \n Press 1 for cname \n Press 2 for cphno \n Press 3 for cmail')
        op=int(input('Enter the number to modify the details : '))
        if op==1:
            cname=input('Enter the new cname : ')
            self.cname=cname
        elif op==2:
            cphno=int(input('Enter the new phone number : '))
            self.cphno=cphno
        elif op==3:
            cmail=input('Enter the mail id : ')
            self.cmail=cmail
        else:
            print('Wrong input')

    @classmethod
    def classmodify(cls):                           #Class method
        print("\nClass objects updation:")
        choice=int(input("Press 1 for Bank name\nPress 2 for Bank's IFSC code\nPress 3 for Managrer name\nEnter the any of the above number to modify the bank details: "))
        if choice==1:
            cls.bname=input('Enter the Bank Name: ')
        elif choice==2:
            cls.ifsc=input('Enter the IFSC code : ')
        elif choice==3:
            cls.mname=input('Enter the manager name: ')
        else:
            print('Invalid input')

# Method - 1
oa=Bank('Ram','7894584565','ram@gmail.com')
oa.disp()
oa.modify()
oa.classmodify()
oa.disp()
print('===' *20)

'''
# Method - 2
oa1=Bank('Raj',4545545454)
Bank.disp(oa1)
Bank.modify(oa1)
Bank.classmodify()
Bank.disp(oa1)
'''