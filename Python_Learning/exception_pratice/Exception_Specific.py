a=10
b= 0
try:
    c = a / b
    print(c)
except ZeroDivisionError:       #specific error as we know user can divide the number by 0
    print('number can not be divided by zero')
except TypeError:
    print("Number cannot be divided by string")
except:
    print("Invalid input")
else:           #block of code to be executed if no errors were raised:
    print("Nothing went worng")
