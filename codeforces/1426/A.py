from sys  import stdin,stdout
from math import ceil
st=lambda:list(stdin.readline().strip())
li=lambda:list(map(int,stdin.readline().split()))
mp=lambda:map(int,stdin.readline().split())
inp=lambda:int(stdin.readline())
pr=lambda n: stdout.write(str(n)+"\n")

mod=1000000007

def solve():
    n,x=mp()
    if n<=2:
        pr(1)
        return
    n-=2
    ans=ceil(n/x) +1
    pr(ans)
    
    


for _ in range(inp()):
    solve()
