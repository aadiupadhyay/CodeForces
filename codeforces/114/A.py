from sys  import stdin,stdout

st=lambda:list(stdin.readline().strip())
li=lambda:list(map(int,stdin.readline().split()))
mp=lambda:map(int,stdin.readline().split())
inp=lambda:int(stdin.readline())
pr=lambda n: stdout.write(str(n)+"\n")
from  math import floor
mod=1000000007
INF= float('inf')
def solve():
    n=inp()
    l=inp()
    base=n
    c=1
    while base<=l:
        if base==l:
            pr('YES')
            pr(c-1)
            return 
        base*=n
        c+=1
    pr('NO')
  
for _ in range(1):
    solve()
