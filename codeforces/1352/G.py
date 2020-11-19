from sys  import stdin,stdout
from collections  import *
from math import gcd,floor,ceil
st=lambda:list(stdin.readline().strip())
li=lambda:list(map(int,stdin.readline().split()))
mp=lambda:map(int,stdin.readline().split())
inp=lambda:int(stdin.readline())
pr=lambda n: stdout.write(str(n)+"\n")

mod=1000000007
INF=float('inf')

def solve():
    n=inp()
    if n<=3:
        pr(-1)
        return
    if n==4:
        print('3 1 4 2')
        return
    ans=[]
    for i in range(1,n+1,2):
        ans.append(i)
    x=i-3
    ans.append(x)
    if n%2==0:
        ans.append(n)
    ans.append(x+2)
    x-=2
    while x>=2:
        ans.append(x)
        x-=2
    print(*ans)

        
            
    
for _ in range(inp()):
    solve()
