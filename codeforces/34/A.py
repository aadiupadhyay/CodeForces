def solve():

    n=int(input())
    l=list(map(int,input().split()))
    d={}
    d[1]=abs(l[0]-l[-1])
    maxx=10000
    for i in range(1,n):
        d[i+1]=abs(l[i]-l[i-1])
    for i,j in d.items():
        if j<maxx:
            maxx=j
            pair=i
    if pair==1:
        print(pair,n)
    else:
        print(pair,pair-1)
        
        
solve() 
