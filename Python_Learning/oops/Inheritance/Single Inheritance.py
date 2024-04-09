class A:            #Parent class
    a=30
    b=40
class B(A):         #Child Class
    c=50
    d=60

a1=A()
b1=B()
print(A.a,A.b)
print(a1.a,a1.b)

print(B.a,B.b,B.c,B.d)
print(b1.a,b1.b,b1.c,b1.d)

print("Modification w.r.t Parent class")
A.a=500
print(A.a,A.b)
print(a1.a,a1.b)

print(B.a,B.b,B.c,B.d)
print(b1.a,b1.b,b1.c,b1.d)

print("Modification w.r.t Child class")
B.a=600
print(A.a,A.b)
print(a1.a,a1.b)

print(B.a,B.b,B.c,B.d)
print(b1.a,b1.b,b1.c,b1.d)