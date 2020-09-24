from sys  import stdin,stdout
from  collections import Counter
st=lambda:list(stdin.readline().strip())
li=lambda:list(map(int,stdin.readline().split()))
mp=lambda:map(int,stdin.readline().split())
inp=lambda:int(stdin.readline())
pr=lambda n: stdout.write(str(n)+"\n")

mod=1000000007
INF= float('inf')

def SET(n):
    i=32
    while not n&(1<<i):
        i-=1
    return i

def solve():
    n=inp()
    l=li()
    x=[]
    for i in l:
        x.append(SET(i))
    d=Counter(x)
    ans=0
    for j in d:
        i=d[j]
        ans+= (i*(i-1))//2
    pr(ans)
for _ in range(inp()):
    solve()
