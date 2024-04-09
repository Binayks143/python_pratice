class Bank:
    bname="HDFC"
    mname="Binay"
    ifsc='HDFC10214'
    def __init__(self,cname,cphno,cage,cmail=None):
        self.cname=cname
        self.cphno=cphno
        self.cage=cage
        self.cmail=cmail
oa=Bank('ram','985456666',65,'abc@gmail.com')
oa1=Bank('ajay','6665656666',66)
print(oa.bname,oa.mname,oa.ifsc,oa.cname,oa.cphno,oa.cage,oa.cmail)
print(oa1.bname,oa1.mname,oa1.ifsc,oa1.cname,oa1.cphno,oa1.cage,oa1.cmail)

    
