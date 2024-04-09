#Exceptional Handling
a=5
b=0
try:
    c=a/b       #compiler will try to execute this statement if it works fine else we have to write except block
except Exception:       #this will excecute only when try give error
    print('You can not divid the number by 0')
print('Bye')

#e.g:2
a=8
b=0
try:
    c=a/b
except Exception as e:      #use to print the actual message
    print('You can not divid the number by 0',e)
print('Bye')
