from sys  import stdin,stdout

#from collections import defaultdict

st=lambda:list(stdin.readline().strip())
li=lambda:list(map(int,stdin.readline().split()))
mp=lambda:map(int,stdin.readline().split())
inp=lambda:int(stdin.readline())
pr=lambda n: stdout.write(str(n)+"\n")

#from bisect import bisect_left,bisect_right

mod=1000000007
INF=float('inf')

def solve():
    n,k=mp()
    l=li()
    l.sort()
   
    ans=0
    a=l[0]
    for i in range(1,n):
        if l[i]<=k:
            ans+=(k-l[i])//a
    pr(ans)
            

for _ in range(inp()):

    solve()
