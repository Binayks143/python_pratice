class A:
    a=10
class B:
    a=20
class C(A,B):
    b=25
    c=35
print(A.a)
print(B.a)
print(C.a,C.b,C.c)

print('Modification w.r.t first inherated class(B)')
B.a=22
print(A.a)
print(B.a)
print(C.a,C.b,C.c)

print('Modification w.r.t lastly inherated class (A)')
A.a=122
print(A.a)
print(B.a)
print(C.a,C.b,C.c)