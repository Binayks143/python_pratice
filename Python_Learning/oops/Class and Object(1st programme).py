class test:
    a=20
    b=30
oa=test()
ob=test()
print(test.a,test.b)
print(oa.a,oa.b)
print(ob.a,ob.b)
print('Modification wrt class')
test.a=50
print(test.a,test.b)
print(oa.a,oa.b)
print(ob.a,ob.b)
print('Modification wrt oa')
oa.a=80
print(test.a,test.b)
print(oa.a,oa.b)
print(ob.a,ob.b)
print('Modification wrt to ob')
ob.a=100
print(test.a,test.b)
print(oa.a,oa.b)
print(ob.a,ob.b)
print('Again modification wrt class')
test.a=150
test.b=200
print(test.a,test.b)
print(oa.a,oa.b)
print(ob.a,ob.b)

'''
print(id(oa))
print(id(ob))
print(id(test))
'''
print(oa.a.bit_length())
