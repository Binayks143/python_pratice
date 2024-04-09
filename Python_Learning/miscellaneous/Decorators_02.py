def mail(func):
    def recepients(name):
        print('Dear',name)
        func()
        print("Thanks & Regards")
    return recepients
@mail
def team():
    print("You are sortlisted for final game\n")

a=['ram','Bablu','Sohan','Ronak']
for i in a:
    team(i)
