A=list(map(int,input().split()))
B=list(map(int,input().split()))
C=list(map(int,input().split()))
a=0
b=0
c=0
d=float("inf")
an=len(A)
bn=len(B)
cn=len(C)
while (a<an and b<bn and c<cn):
    d=min(d,max(A[a],B[b],C[c])-min(A[a],B[b],C[c]))
    if A[a]<B[b]:
        if(A[a]<C[c]):
            a+=1
        else:
            c+=1
    else:
        if B[b]<C[c]:
            b+=1
        else:
            c+=1
print(d)
