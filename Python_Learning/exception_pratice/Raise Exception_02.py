def test(p):
    i=0
    while i<p:
        result=i**2
        yield result
        i+=1
        raise StopIteration('Reached maximun value')
n=test(5)

for i in range(6):
    print(next(n))