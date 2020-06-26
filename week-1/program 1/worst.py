l=list(map(int,input().split()))
xor_array=[]
n=len(l)
queries=[[0,1],[1,2],[0,3],[3,3]]
nq=len(queries)
for l1 in queries:
    ans=0
    for i in range(l1[0],l1[1]+1):
        ans=ans^l[i]
    print(ans,end=" ")
        
