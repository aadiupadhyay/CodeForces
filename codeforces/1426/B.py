from sys  import stdin,stdout
from math import ceil
st=lambda:list(stdin.readline().strip())
li=lambda:list(map(int,stdin.readline().split()))
mp=lambda:map(int,stdin.readline().split())
inp=lambda:int(stdin.readline())
pr=lambda n: stdout.write(str(n)+"\n")

mod=1000000007

def solve():
    n,m=mp()
    f=0
    for i in range(n):
        a,b=mp()
        c,d=mp()
        if b==c:
            f=1
    if m&1:
        pr('NO')
    else:
        if f:
            pr('YES')
        else:
            pr('NO')


for _ in range(inp()):
    solve()
