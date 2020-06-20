def solve():

    n,m=map(int,input().split())
    l=list(map(int,input().split()))
    l.sort()
    c=0
    for i in range(m):
        if l[i]<0:
            c-=l[i]
    print(c)
        
solve() 
