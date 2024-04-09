def stn(m,n):
    print(n[m], end=' ')
    if m<len(n)-1:
        stn(m+1,n)
       # print(n[m], end=' ')


n= str (input("Enter the String: "))
m= int(input("Enter the index: "))
stn (m,n)