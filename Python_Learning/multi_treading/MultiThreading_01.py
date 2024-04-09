from threading import *
#importing everything from threading package
from time import sleep
class test(Thread):     #test is subclass of Thread
    def run(self):              #run is mandatory beacuse for start it calls run internally
        for i in range(150):
            print("Hello")
            sleep(0.5)

class test1(Thread):
    def run(self):
        for i in range(150):
            print("hiii")
            sleep(0.5)

t1=test()
t2=test1()
#t1.run()      #it will print from class test only here threading will not start
#t2.run()
t1.start()    #It arranges for the object's run() method to be invoked, here threading will start
sleep(0.1)      #to avoid collision
t2.start()
print("bye")
