from sys  import stdin,stdout
from math import ceil
st=lambda:list(stdin.readline().strip())
li=lambda:list(map(int,stdin.readline().split()))
mp=lambda:map(int,stdin.readline().split())
inp=lambda:int(stdin.readline())
pr=lambda n: stdout.write(str(n)+"\n")

mod=1000000007
INF=float('inf')

def solve():
    n=inp()
    now= n
    nex= n-1
    ans=[]
    for i in range(n-1):
        ans.append((now,nex))
        now= ceil((nex+now)/2)
        nex-=1
    val= ceil(sum(ans[-1])/2)
    print(val)
    for i in ans:
        print(*i)

for _ in range(inp()):

    solve()
