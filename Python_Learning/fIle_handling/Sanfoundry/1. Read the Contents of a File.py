file1=input("Enter the file name with extension: ")

file=open(file1,'r')
temp=file.readline()
while(temp!=""):
    print(temp)
    temp=file.readline()
file.close()
