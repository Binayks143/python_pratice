class A:
    a=10
    b=20
class B(A):
    c=30
class C(A):
    d=40
class hybrid(B,C):
    e=50

print(A.a,A.b)
print(B.a,B.b,B.c)
print(C.a,C.b,C.d)
print(hybrid.a,hybrid.b,hybrid.c,hybrid.d,hybrid.e)

print('Modification w.r.t parent class A')
A.a=15
print(A.a,A.b)
print(B.a,B.b,B.c)
print(C.a,C.b,C.d)
print(hybrid.a,hybrid.b,hybrid.c,hybrid.d,hybrid.e)

print('Modification w.r.t child class B')
B.a=25
print(A.a,A.b)
print(B.a,B.b,B.c)
print(C.a,C.b,C.d)
print(hybrid.a,hybrid.b,hybrid.c,hybrid.d,hybrid.e)

print('Modification w.r.t hybrid class: ')
hybrid.a=500
print(A.a,A.b)
print(B.a,B.b,B.c)
print(C.a,C.b,C.d)
print(hybrid.a,hybrid.b,hybrid.c,hybrid.d,hybrid.e)
