#if location is not maintioned it will take default location
print("Start the writing")
f=open("Test1.txt",'w')
f.write("Hii how are you?")
#f.close()
print("Start the reading")
f1=open("Test1.txt",'r')
print(f1.read())

#here writing started but not able to read because file is open for reading the file it must be closed

#Another way to open and read the files With "As" keyword
#here no worry about closing the file
print("With As keyword Write/Read")
with open("test2.txt",'w') as f2_write:
    f2_write.write("Doing Expriments")
print("\nWriting done\nNow reading the file\n")
with open("test2.txt",'r') as f2_read:
    print(f2_read.read())


