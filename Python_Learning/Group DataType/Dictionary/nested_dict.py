"""
Nested Dictionary : dictionay under dictionary
d={cars:{'model':'Ritz','Year':2009},bike:{'Brand':'Honda','Year':2020}

"""

d={'cars':{'model':'Ritz','Year':2009},'bike':{'Brand':'Honda','Year':2020}}
print(d)
print(d['cars'])
print(d['cars']['Year'])
print(d.values())
print(d.keys())
print(d.items())
d1=d.copy()
print("d1=", d1)
d1.clear()
print(d1)

