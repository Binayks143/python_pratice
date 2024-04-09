class Bank:
    bname='HDFC'
    mname='Rahul'
    Ifsc='HDFC00122'
    def __init__ (self,cname,cage,cphno,cmail=None):
        self.cname=cname
        self.cage=cage
        self.cphno=cphno
        self.cmail=cmail

    def disp(self):
        print ("Bname is" , self.bname)
        print ("Mname is" , self.mname)
        print ("IFSC COde is" , self.Ifsc)
        print ("Cname is" , self.cname)
        print ("C Age is" , self.cage)
        print ("Cph no is" , self.cphno)
        print ("Cmail is" , self.cmail)
        print('-------------------------')
oa= Bank('RAM','28','985444566')
oa1= Bank ('Bijay','47','6556565698','abc@gmail.com')
oa.disp()
oa1.disp()
oa.cname='Binay'
oa.disp()




