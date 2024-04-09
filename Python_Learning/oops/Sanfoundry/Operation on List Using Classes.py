#

class A:
    def __init__(self):
        self.l = [1,2,8,'llll']
    def append(self,n1):
        self.l.append(n1)
        return self.l
    def delete(self,n2):
        self.l.remove(n2)
        return self.l
    def disp(self):
        return self.l
print('1 : Adding the element to the list\n')
print('2 : Deleting the element to the list\n')
print('3 : Display the list elements\n')
a=int(input ('Select the option to perform action: '))
oa=A()
if a==1:
    print("List element is",oa.l)
    a1=input('ENter the element to add in list: ')
    oa.append(a1)
    print(oa.l)

elif a==2:
    print("List element is", oa.l)
    p=input("Which element you want to delete: ")
    oa.delete(p)
    print(oa.l)
elif a==3:
    print('List elements is ',oa.disp())
else:
    print('wrong input please try again')



