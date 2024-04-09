class bank:
    #Generic Data
    bname='HDFC'
    mname='Hari'
    ifsc='HDFC1254'
    #Specific Data of customer, (email is option)
    def __init__(self,cname,cphone,email=None): #for option field we have to user None
        self.cname=cname
        self.cphone=cphone
        self.email=email

oa=bank('binay',7874545856,'binay@gmail.com')
oa1=bank('jay',545454222)
print('Bank name is', oa.bname, ",Bank's Manager name is", oa.mname,',Bank IFSC code is ', oa.ifsc,
      ',Customer name is ', oa.cname,',customer contact number is ', oa.cphone ,'and customer mail id is',oa.email)
print('Bank name is', oa1.bname, ",Bank's Manager name is", oa1.mname,',Bank IFSC code is ', oa1.ifsc,
      ',Customer name is ', oa1.cname,',customer contact number is ', oa1.cphone ,'and customer mail id is',oa1.email)