#is a relation ship (Inheritance)
class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def behaviour(self):
        print("Daily routin is wake up, fresh up, have a breakfast, go to office etc")

class emp(person):
    def __init__(self,name,age,phno,sal):
        super().__init__(name,age)
        self.phno=phno
        self.sal=sal

    def work(self):
        print('I am a software engineer')

    def empinfo(self):
        print('Name of the employee:',self.name)
        print('Age of the employee is ',self.age)
        print('Phone number of the emp is',self.phno)
        print('Salary of the employee is',self.sal)

o1=emp('Raj',25,543455445,520000)
o1.behaviour()
o1.work()
o1.empinfo()
