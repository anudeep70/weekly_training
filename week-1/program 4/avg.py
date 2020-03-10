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
def minNoOfRepalcemets(n):
    count=0
    while n!=1:
        if n%2==0:
            n=n//2
        else:
            n=n-1
        count+=1
    return count
while True:
    print(minNoOfRepalcemets(int(input())))
