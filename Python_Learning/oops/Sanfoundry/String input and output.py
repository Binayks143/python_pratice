#Python Program to Create a Class in which One Method Accepts a String from the User and Another Prints it

class String_print:

    def get(self):
        self.n=str(input("Enter the String: "))

    def output(self):
        print("Entered String is :",self.n)


s1=String_print()
s1.get()
s1.output()