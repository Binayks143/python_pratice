#file file123 is not available

fw=open(r'file123.txt','w')
print(fw)       # file with name file123 created
fw.write("Hari om baba")
fw.close()

# #varifying the write data
# fw=open(r'file123.txt','r')
# print(fw.read())
# fw.close()
#
# #It will over write the existing file
# fw=open(r'file123.txt','w')
# fw.write("jai ho")
# print(fw.writable())        #gives the boolean result if open true else close
#
# fw.close()
#
# fw=open(r'G:\Python file handling\file123.txt','r')
# print(fw.read())
# fw.close()
# print(fw.writable())        # no because it closed
#
# fw=open(r'G:\Python file handling\file123.txt','w')
# fw.writelines("using to write the line\nhii\nhello")
# fw.close()
# fw=open(r'G:\Python file handling\file123.txt','r')
# print(fw.read())
# fw.close()
#
#
#
#
