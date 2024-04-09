f1=open('file123.txt','r')
#print(f1.read())                #Read whole file
print(f1.read(10))                #read first 10 char
#print(f1.readline())            #Read first line
#print(f1.readline(3))          #read first 15 char
#print(f1.readline(50000))       #if files doesnot have 50000 char its give only first line.
#print(f1.readable())            # return true and false
#print(f1.readlines())           # give the ouput in list format
#print(f1.readlines(1000))      #give first output in list
#print(f1.name)                  # give file location with name
#print(f1.mode)                  #Give which mode its open
#print(f1)                       # gives file info
print(f1.tell())                  #give the current cursor position
f1.seek(2)                         # move the cursor to required position
#print(f1.tell())
# used to print from line x to line y
d=f1.readlines()
for i in range(0,2):
    print(d[i])
print(type(d))
#
# print(f1.tell())

f1.close()                        #used to close the file
print(f1.closed)                  # used to check wheather file is closed or not
