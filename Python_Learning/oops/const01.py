class Bank:
    bname="HDFC"
    mname="Binay"
    ifsc='HDFC10214'
    def __init__(self,cname,cphno):
        self.cname=cname
        self.cphno=cphno
oa=Bank('ram','985456666')
oa1=Bank('ajay','6665656666')
print(oa.bname,oa.mname,oa.ifsc,oa.cname,oa.cphno)
print(oa1.bname,oa1.mname,oa1.ifsc,oa1.cname,oa1.cphno)

    
