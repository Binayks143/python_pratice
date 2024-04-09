#When there is no exception
a=5
b=4
try:
    print("DB Connection open")
    print(a/b)
    print("DB Connection CLose")
except Exception as e:
    print('You can not divide a number with zero,',e)

#When there is exception occurs
a=5
b=0
try:
    print("\nDB1 Connection open")
    print(a/b)                          #exception occurs
    print("DB1 Connection CLose") #if excen occurs it will skip this statement and jump to excep block
except Exception as e:
    print('You can not divide a number with zero\n')
#SO here we are not able to close the DB

#When there is exception occurs and trying to close the db
a=5
b=0
try:
    print("DB2 Connection open")
    print(a/b)                          #exception occurs
except Exception as e:
    print('You can not divide a number with zero')
    print("DB2 Connection CLose\n")

#in the above programe db is opening and closing fine
#When there is again exception will not occurs
a=5
b=3
try:
    print("DB3 Connection open")
    print(a/b)                          #exception occurs
except Exception as e:
    print('You can not divide a number with zero')
    print("DB3 Connection CLose")       #Here DB is not closing

#Note: in the above eg we have see there is diffuculty to close the DB, so for that we can use finally keyword
#and solve the above problems
a=5
b=0
try:
    print("\nDB4 Connection open")
    print(a/b)                          #exception occurs
except Exception as e:
    print('You can not divide a number with zero')
finally:            # Doesnot matter wheater we will get exception or not
    print("DB4 Connection CLose")


