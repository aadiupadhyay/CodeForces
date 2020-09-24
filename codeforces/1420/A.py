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
    n=inp()
    l=li()
    f=0
    for i in range(1,n):
        if l[i]>=l[i-1]:
            f=1
            break   
    if f==0:
        pr('NO')
    else:
        pr('YES')
    
for _ in range(inp()):
    solve()
