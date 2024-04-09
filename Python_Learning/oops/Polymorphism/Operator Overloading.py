class student:
    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2
    def disp(self):
        print(self.m1,self.m2)

    def __add__(self, other):
        m1=self.m1+other.m1
        m2=self.m2+other.m2
        return (student(m1,m2))

    def __str__(self):
        #return self.m1,self.m2      #output in the form of tuple while printing print(s) we will get type error that is string type is not returning
       return '{} {}'.format(self.m1,self.m2)


s1=student(55,58)
s2=student(60,99)
s1.disp()
s2.disp()
s=s1+s2                 #student __add__(s1,s2)
print(s.m1,s.m2)
# in general programming
a=5
print(a)
print(a.__str__())
#in above to print it will give same output while using print(a) interpreater by deafult adding
# __ str__()
print(s.__str__())
#here it will print address (if def is not defiend) because in this class __str__ is not defiend so we have to override this method in object __str__ is giving module name. class name address

#print(s)    #type error beacuse we are not returning string object

print(s)





