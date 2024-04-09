#same as apped but here we can do append and read
a1=open(r"G:\Python file handling\file1234.txt",'a+')
print("Cursor position before writing the data:",a1.tell())
data=a1.write("this is new file, appending the data in new file\n")
print("data block size is appeded",data)
print("Cursor position after writing the data:",a1.tell())
a1.seek(0)          #movingthe cursor to 0 position to read the data from starting
print(a1.read())
a1.close()
