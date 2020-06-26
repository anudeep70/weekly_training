def countBits(num):
    if num==0:
        return [0,]
    ans=[0,1,]
    for i in range(2,num+1):
        if (i & i-1)==0:
            index=0
        ans.append(ans[index]+1)
        index+=1
    return ans
while True:
    print(countBits(int(input())))
