#Python Program to Take in the Marks of 5 Subjects and Display the Grade

H= float(input("Enter the Hindi mark :"))
M= float(input("Enter the Math mark :"))
E= float(input("Enter the English mark :"))
P= float(input("Enter the Physics mark :"))
C= float(input("Enter the Chemistry mark :"))

Total=round(H+M+E+P+C)
Avg=Total/5
print("The total mark of the student is ",Total,"And the average is",Avg, "%")

if Avg >=100:
    print ("Invalid Avg")
elif Avg>=70:
    print ("Result is First")
elif Avg >=50:
    print("Result is Second")
elif Avg >=30:
    print ("Result is Third")
else:
    print ("Result is Fail")
