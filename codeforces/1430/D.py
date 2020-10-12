from sys  import stdin,stdout
from bisect import bisect_left
st=lambda:list(stdin.readline().strip())
li=lambda:list(map(int,stdin.readline().split()))
mp=lambda:map(int,stdin.readline().split())
inp=lambda:int(stdin.readline())
pr=lambda n: stdout.write(str(n)+"\n")

mod=1000000007
INF=float('inf')

def solve():
    n=inp()
    x=[1]
    s=st()
    i=0
    for i in range(1,n):
        if s[i]==s[i-1]:
            x[-1]+=1
        else:
            x.append(1)

    ans=len(x)
    i=0
    j=0
    l=len(x)
    while i<l:
        while j< len(x) and x[j]==1:
            j+=1
        if j<len(x):
            x[j]-=1
        else:
            l-=1
            l=max(i+1,l)
        i+=1
        j=max(i,j)
    ans-=(len(x)-l)
    pr(ans)
for _ in range(inp()):

    solve()
