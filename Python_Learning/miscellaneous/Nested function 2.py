#FUnction inside a function is called nested func or inner functn

def disp(n):
    def disp1():
        print("Display 1 func")
        return 1
    def disp2():
        print("Display 2 func")
    if n==1:
        return disp1()
    else:
        return disp2()

disp(1)
disp(2)
print(disp(1))
print(disp(2))

