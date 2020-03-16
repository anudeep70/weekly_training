def validPram(n,s,leftcount,rightcount):
    if leftcount==rightcount==n:
        print(s)
    if leftcount<=n:
        validPram(n,s+"(",leftcount+1,rightcount)
    if leftcount>rightcount:
        validPram(n,s+")",leftcount,rightcount+1)
while True:
    validPram(int(input())//2,"",0,0)
