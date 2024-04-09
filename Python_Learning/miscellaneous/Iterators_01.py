a=[1,2,3,'Hello']

#1st way using index
print("1st way")
print(a[1])

#2nd Way using loop
print("2nd way")
for i in a:
    print(i)
#3rd way using iterator
print("3rd way")

j=iter(a)
print(j)        #printing object of iterator
print(next(j))
print(next(j))
print(next(j))
print(next(j))

#4th way using iterator
print("4th way")

it=iter(a)
print(it.__next__())
print(it.__next__())
print(it.__next__())
print(it.__next__())
