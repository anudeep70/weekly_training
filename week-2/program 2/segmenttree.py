a=[-1 for i in range(1000)]
l=[]
def builtsegmentTree(l,index,start,end):
    if start==end:
        a[index]=l[start]
        return l[start]
    if start>end:
        return 0
    mid=(start+end)//2
    a[index]=builtsegmentTree(l,2*index+1,start,mid)+builtsegmentTree(l,2*index+2,mid+1,end)
    return a[index]
def sumOfRange(a,index,start,end,s,e):
    if start==s and end==e:
        return a[index]
    mid=(start+end)//2
    if s>mid:
        return sumOfRange(a,2*index+2,mid+1,end,s,e)
    if e<=mid:
        return sumOfRange(a,2*index+1,start,mid,s,e)
    return sumOfRange(a,2*index+1,start,mid,s,mid)+sumOfRange(a,2*index+2,mid+1,end,mid+1,e)
def update(a,index,start,end,ui,value):
    if start==end==ui:
        ans=a[index]
        a[index]=value
        return a[index]-ans
    mid=(start+end)//2
    if ui>mid:
        ans=update(a,2*index+2,mid+1,end,ui,value)
        a[index]+=ans
        return ans
    if ui<=mid:
        ans=update(a,2*index+1,start,mid,ui,value)
        a[index]+=ans
        return ans
    
l=list(map(int,input().split()))
n=len(l)
builtsegmentTree(l,0,0,n-1)
print("segment tree as array",a[:2*n-1])
print("sum is : ",sumOfRange(a,0,0,n-1,int(input("enter start index:")),int(input("enter end index"))))
update(a,0,0,n-1,int(input("enter update index:")),int(input("enter value:")))
print("segment tree as array",a[:2*n-1])
print("sum is",sumOfRange(a,0,0,n-1,int(input("enter start index:")),int(input("enter end index:"))))
