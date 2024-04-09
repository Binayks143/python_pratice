class student:
    school='Khalsa'                     #Class(static) Variable
    Exam="10th class"                   #Class(static) Variable
    def __init__(self,math,sci,eng):
        self.math=math                  #instance Variable
        self.sci=sci
        self.eng=eng
    def disp(self):                     #instance Class
        print(student.Exam,"Marks:\nMath=",self.math,'\nScience=',self.sci,'\nEnglish=',self.eng)
        return (self.math+self.sci+self.eng)/3
    @classmethod
    def getschool(cls):                 #class method
        return cls.school

    @staticmethod
    def info():                         #static method
        p="Good Luck"
        return p

s1=student(88,99,50)
s2=student(44,99,88)
print(student.getschool())
print("Average=",s1.disp())
print('='*30)
print("Average=",s2.disp())
print(student.info())