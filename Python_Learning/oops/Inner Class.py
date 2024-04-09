#Telesko 54: Inner class

class bank:                             #Outer Class
    def __init__(self,cname,phno):
        self.cname=cname
        self.phno=phno
        self.s=self.service()           #to create the object of inner class

    def disp(self):                     #outer class disp()
        print('Customer name is :',self.cname,'and','Phone no. is: ',self.phno)
        self.s.disp()

    class service:                      #inner class
        def __init__(self):
            self.s1='ATM'
            self.s2='Internet Banking'
            self.s3='Mobile Banking'

        def disp(self):                 #inner class disp()
            print('Services are:\n',self.s1,'\n',self.s2,'\n',self.s3)

c1=bank('Raju',4545454554)
c1.disp()
# s=bank.service()          #object is at ootside the outer class
# s.disp()                  #To call inner call disp()
#print(c1.s.s2) #            # to access innecr class object

