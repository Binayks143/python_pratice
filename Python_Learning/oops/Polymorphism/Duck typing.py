class BMW:
    def features(self):
        print('Luxury Car')
        print('Very Expensive')
        print('Brand Value')

class Honda:
    def features(self):
        print('Affortable car')
        print('Less servicing')
        print('Attractive colors')

class car:
    def disp(self,brand):
        brand.features()

b1=Honda()
print("Features are:")
c1=car()
c1.disp(b1)