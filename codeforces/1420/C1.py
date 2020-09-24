from sys  import stdin,stdout
from  collections import Counter
st=lambda:list(stdin.readline().strip())
li=lambda:list(map(int,stdin.readline().split()))
mp=lambda:map(int,stdin.readline().split())
inp=lambda:int(stdin.readline())
pr=lambda n: stdout.write(str(n)+"\n")

mod=1000000007
INF= float('inf')

def solve():
    n,q=mp()
    l=li()
    ans=l[0]
    for i in range(1,n):
       
        ans+=max(0,l[i]-l[i-1])

    pr(ans)
for _ in range(inp()):
    solve()
