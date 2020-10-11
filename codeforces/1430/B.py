from sys  import stdin,stdout
from collections import defaultdict
st=lambda:list(stdin.readline().strip())
li=lambda:list(map(int,stdin.readline().split()))
mp=lambda:map(int,stdin.readline().split())
inp=lambda:int(stdin.readline())
pr=lambda n: stdout.write(str(n)+"\n")

mod=1000000007
INF=float('inf')

def solve():
    n,k=mp()
    l=li()
    if n==1:
        pr(0)
        return 
    l.sort()
    i=n-2
    while k!=0 and i>=0:
        l[-1]+=l[i]
        l[i]=0
        i-=1
        k-=1
        
    print(l[-1]-min(l))
        

for _ in range(inp()):

    solve()
