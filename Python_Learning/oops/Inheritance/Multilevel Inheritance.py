class A:                #parent class
    a=10
    b=20

class B(A):             #Child Class
    c=30
    d=40

class C(B):             #SubChild class
    e=50
    f=60

oa=A()
ob=B()
oc=C()

print('Class-A:', 'a=',A.a,',b=',A.b)
print('Object of class-A:', 'a=',oa.a,',b=',oa.b)
print('\nClass-B:', 'a=',B.a,',b=',B.b,',c=',B.c,',d=',B.d)
print('Object of class-B:', 'a=',ob.a,',b=',ob.b,',c=',ob.c,',d=',ob.d)
print('\nClass-C:', 'a=',C.a,',b=',C.b,',c=',C.c,',d=',C.d,',e=',C.e,',f=',C.f)
print('Object of class-C:', 'a=',oc.a,',b=',oc.b,',c=',oc.c,',d=',oc.d,',e=',oc.e,',f=',oc.f)

print('\n\nModification W.r.t parent class here class-A:\n')
A.a=100
print('Class-A:', 'a=',A.a,',b=',A.b)
print('Object of class-A:', 'a=',oa.a,',b=',oa.b)
print('\nClass-B:', 'a=',B.a,',b=',B.b,',c=',B.c,',d=',B.d)
print('Object of class-B:', 'a=',ob.a,',b=',ob.b,',c=',ob.c,',d=',ob.d)
print('\nClass-C:', 'a=',C.a,',b=',C.b,',c=',C.c,',d=',C.d,',e=',C.e,',f=',C.f)
print('Object of class-C:', 'a=',oc.a,',b=',oc.b,',c=',oc.c,',d=',oc.d,',e=',oc.e,',f=',oc.f)

print('\n\nModification w.r.t child class here class-B:\n')
B.a=2000
print('Class-A:', 'a=',A.a,',b=',A.b)
print('Object of class-A:', 'a=',oa.a,',b=',oa.b)
print('\nClass-B:', 'a=',B.a,',b=',B.b,',c=',B.c,',d=',B.d)
print('Object of class-B:', 'a=',ob.a,',b=',ob.b,',c=',ob.c,',d=',ob.d)
print('\nClass-C:', 'a=',C.a,',b=',C.b,',c=',C.c,',d=',C.d,',e=',C.e,',f=',C.f)
print('Object of class-C:', 'a=',oc.a,',b=',oc.b,',c=',oc.c,',d=',oc.d,',e=',oc.e,',f=',oc.f)

print('\n\nModification w.r.t Sub-Child class here class-C:\n')
C.a=3000
print('Class-A:', 'a=',A.a,',b=',A.b)
print('Object of class-A:', 'a=',oa.a,',b=',oa.b)
print('\nClass-B:', 'a=',B.a,',b=',B.b,',c=',B.c,',d=',B.d)
print('Object of class-B:', 'a=',ob.a,',b=',ob.b,',c=',ob.c,',d=',ob.d)
print('\nClass-C:', 'a=',C.a,',b=',C.b,',c=',C.c,',d=',C.d,',e=',C.e,',f=',C.f)
print('Object of class-C:', 'a=',oc.a,',b=',oc.b,',c=',oc.c,',d=',oc.d,',e=',oc.e,',f=',oc.f)