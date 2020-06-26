h={}
def oneInAllThrees(l):
    n=len(l)
    for i in l:
        if i in h:
            h[i]=((h[i]+1)%3)+1
        else:
            h[i]=1
    for i in h:
        if h[i]==1:
            return i
while True:
    h={}
    l=list(map(int,input().split()))
    print(oneInAllThrees(l))
