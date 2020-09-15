from sys  import stdin,stdout
from collections import deque
st=lambda:list(stdin.readline().strip())
li=lambda:list(map(int,stdin.readline().split()))
mp=lambda:map(int,stdin.readline().split())
inp=lambda:int(stdin.readline())
pr=lambda n: stdout.write(str(n)+"\n")

mod=1000000007
def MA(l):
    ma=float('-inf')
    n=len(l)
    a=0
    for i in range(n):
        a+=l[i]
        if a>ma:
            ma=a
        if a<0:
            a=0
            
    return ma

def solve():
    n=inp()
    l=li()
    s=sum(l)

    if s>max(MA(l[:-1]),MA(l[1:])):
        print('YES')
    else:
        print('NO')
        

for _ in range(inp()):
    solve()
