#for append file should be present if not it will creat the file
a1=open(r"G:\Python file handling\file123.txt",'a')
print("Cursor position before writing the data:",a1.tell())
data=a1.write("\nappending the data in existing file enjoy!")
print("data block size is appeded",data)
print("Cursor position after writing the data:",a1.tell())
a1.close()
a1=open(r"G:\Python file handling\file123.txt",'r')
print(a1.read())