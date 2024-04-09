# Anagram (All world contains same characters eg. tea, eat)
'''
def is_anagram(word1,word2):

    if len(w1)==len(w2):
        print("it might be anagram")
        l1=list(w1)
        l2=list(w2)
        print(l1,l2)
        if l1==l2:
            print('yes')
        
w1=input("Enter 1st word")
w2=input("Enter 2nd word")
is_anagram(w1,w2)


#remove Duplicates

def unique_only (iterable):
    unique =set()
    for item in iterable:
        if item not in unique:
            unique.add(item)
    return unique'''

#tail
def tail(i,n):
    return i[-1:-n:-3]
