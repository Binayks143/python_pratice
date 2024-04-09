file='test09.txt'
n=0
with open(file,'r') as f1:
    for i in f1:
        n=n+1
print("nos of lines is ",n)
