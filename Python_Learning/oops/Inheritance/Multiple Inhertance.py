class A:
    a=10
    b=20
class B:
    a=100
    d=40
class C(B,A):
    e=50

print(A.a,A.b)
print(B.a,B.d)
print(C.a,C.b,C.a,C.d,C.e)
