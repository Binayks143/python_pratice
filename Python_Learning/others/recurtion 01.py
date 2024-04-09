def rec(n):
    print(n,end=' ')
    if n>1:
        rec(n-2)
rec(15)
