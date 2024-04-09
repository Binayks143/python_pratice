class fruit:
    def __init__(self):
        print("Available everywhere,easy to consume")

    def nutrition(self):
        print("Good for health")

    def fruit_shape(self):
        print("fruit: different shapes are available")
class mango(fruit):
    def __init__(self):
        fruit.__init__(self)
        print("available in summer season")

    def nutrition(self):
        super(mango, self).nutrition()
        print("Mango is Highly nutrious")

    def color(self):
        print("Green, ripe mangoes are yellow")

m1=mango()
m1.nutrition()
m1.fruit_shape()
m1.color()
