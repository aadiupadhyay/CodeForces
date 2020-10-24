from sys  import stdin,stdout
from collections  import *
from math import *
st=lambda:list(stdin.readline().strip())
li=lambda:list(map(int,stdin.readline().split()))
mp=lambda:map(int,stdin.readline().split())
inp=lambda:int(stdin.readline())
pr=lambda n: stdout.write(str(n)+"\n")

mod=1000000007
INF=float('inf')

def solve():
    n=inp()
    l=[[0 for i in range(n)] for j in range(n)]
    if n&1:
        l[0][n//2]=1
        l[n//2][0]=1
        l[n//2][n//2]=1
    for i in range(n//2):
        l[i][i]=1
        l[n-1-i][i]=1
        l[i][n-i-1]=1
        l[n-i-1][n-i-1]=1
    for i in l:
        print(*i)
    
for _ in range(inp()):
    solve()
