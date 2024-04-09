#This is use to override the address of one function to another function

def disp():
    print('Inside disp')

def disp1():
    print('Inside disp1')

disp()
print(id(disp))
disp1()
print(id(disp1))

print('After Monkey Patching')
disp=disp1
disp()
print(id(disp))
disp1()
print(id(disp1))

