l=list(map(int,input().split()))
n=len(l)
queries=[[0,1],[1,3],[0,3],[3,3]]
nq=len(queries)
while True:
    ans=0
    xor_array=[]
    for i in range(n):
        ans=ans ^ l[i]
        xor_array.append(ans)
    print(xor_array)
    for l1 in queries:
        if l1[0]!=0:
            print(xor_array[l1[1]]^xor_array[l1[0]-1],end=" ")
        else:
            print(xor_array[l1[1]],end=" ")
    print()
    l=list(map(int,input().split()))
