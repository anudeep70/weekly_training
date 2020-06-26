def maxXor(l):
    n=len(l)
    m=float("-inf")
    for i in range(n-1):
        for j in range(i,n):
            m=max(m,l[i]^l[j])
    return m
while True:
    l=list(map(int,input().split()))
    print(maxXor(l))
