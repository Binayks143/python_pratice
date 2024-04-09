#FUnction inside a function is called nested func or inner functn

def start():
    print("Process is starting")

    def finish():
        print("Completing the process")
    def pickup():
        print("Picking the raw materials")
    def mix():
        print("Mixing  the materials")
    pickup()
    mix()
    finish()

start()
