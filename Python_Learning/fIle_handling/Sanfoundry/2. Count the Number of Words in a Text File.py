file='test09.txt'

n=0
with open(file,'r') as f1:
    for line in f1:
        words=line.split()
        n=n+len(words)
print("No of words are :",n)