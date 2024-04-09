r=open("G:\Python file handling\Screenshot_3.jpg",'rb')
#print(r.read())     #return th eresult in binary format


r1=open(r"G:\Python file handling\n3.jpg",'wb')

for i in r:     #copy the contens of r object in r1 object
    r1.write(i)
r.close()
r1.close()