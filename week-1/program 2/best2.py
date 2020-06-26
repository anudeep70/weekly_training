for _ in range(10):
    a,b,c=map(int,input().split())
    d=(a | b)^c
    g=(a & b & c) ^ (a&b)
    c=0
    while (d!=0):
        c+=1
        d=d&d-1
    while (g!=0):
        c+=1
        g=g&g-1
    print(c)
