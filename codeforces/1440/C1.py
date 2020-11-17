from sys  import stdin,stdout
from collections  import *
from math import gcd,floor,ceil
from bisect import bisect_left as bl
st=lambda:list(stdin.readline().strip())
li=lambda:list(map(int,stdin.readline().split()))
mp=lambda:map(int,stdin.readline().split())
inp=lambda:int(stdin.readline())
pr=lambda n: stdout.write(str(n)+"\n")

mod=1000000007
INF=float('inf')

def solve():
    n,m=mp()
    ans=[]
    l=[st() for i in range(n)]
    for i in range(n):
        for j in range(m):
            if l[i][j]=='1':
                x,y=1,1
                if i==n-1:
                    x*=-1
                if j==m-1:
                    y*=-1
                ans.append([i+1,j+1,i+x+1,j+1,i+x+1,j+y+1])
                ans.append([i+1,j+1,i+1,j+y+1,i+x+1,j+y+1])
                ans.append([i+1,j+1,i+x+1,j+1,i+1,j+y+1])
    pr(len(ans))
    for i in ans:
        print(*i)
             
for _ in range(inp()):
    solve()

