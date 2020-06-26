""" 4.Given a positive integer n and you can do operations as follow:
1.	If n is even, replace n with n/2.
2.	If n is odd, you can replace n with either n + 1 or n - 1.
What is the minimum number of replacements needed for n to become 1?
Example 1:
Input:
8

Output:
3

Explanation:
8 -> 4 -> 2 -> 1
5.Given a non negative integer number num. For every numbers i in the range 0 ≤ i ≤ num calculate the number of 1's in their binary representation and return them as an array.
"""
dic={}
def minReplace(n):
    if n==1:
        return 0
    if n<=0:
        return float("inf")
    if n in dic:
        return dic[n]
    if n%2==0:
        dic[n]=minReplace(n//2)+1
        return dic[n]
    else:
        dic[n]=min(minReplace(n+1),minReplace(n-1))+1
        return dic[n]
    return minReplace(n)
print(minReplace(int(input())))
