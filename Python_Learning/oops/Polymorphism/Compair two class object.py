class A:
    def __init__(self,n):
        self.n=n
    def __gt__(self, other):
        n1=self.n
        n2=other.n
        if n1>n2:
            return True
        else:
            return False

oa=A(15)
ob=A(18)
if (oa>ob):
    print("Oa is greater")
else:
    print("Ob is greater")