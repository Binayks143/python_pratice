class car:                        #has a relationship beacuse we are not extending the functionality
    def __init__(self,bname,model,color):
        self.bname=bname
        self.model=model
        self.color=color

    def carinfo(self):
        print('Brand of the car:{}\nModel of the car:{}\nColor of the car:{}'.format(self.bname,self.model,self.color))

c1=car('BMW','Q7','RED')
c2=car('Audi',7854,'Black')
c1.carinfo()
c2.carinfo()

class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def behavior(self):
        print('Daily routin like wake up, fresh up, having breakfast , go to office etc')

class emp(person):      #is a retionship because we are extending the functionality
    def __init__(self,name,age,phno,sal):
        super().__init__(name,age)
        self.phno=phno
        self.sal=sal

    def work(self):
        print('Software Engineer')

    def empinfo(self):
        print('Employee name is:{},age is {}\nPhone number is:{}\nSalery is {}'.format(self.name,self.age,self.phno,self.sal))

e1=emp('Binay',28,57487545454,25000)
e1.behavior()
e1.work()
e1.empinfo()