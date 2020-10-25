from sys  import stdin,stdout
from collections  import *
from math import ceil, floor
st=lambda:list(stdin.readline().strip())
li=lambda:list(map(int,stdin.readline().split()))
mp=lambda:map(int,stdin.readline().split())
inp=lambda:int(stdin.readline())
pr=lambda n: stdout.write(str(n)+"\n")

mod=1000000007
INF=float('inf')

def solve():
    n,m=mp()
    row,col=[],[]
    r,c={},{}
    ans=[[0 for i in range(m)] for j in range(n)]
    for i in range(n):
        l=li()
        r[l[0]]=l
        row.append(l)
    for i in range(m):
        l=li()
        c[l[0]]=l
        col.append(l)
    f=0
    for i in row:
        a=i[0]
        for j in col:
            b=j[0]
            if a==b:
                val=i
                f=1
                break
        if f:
            break
    for i in range(m):
        ans[0][i]=val[i]
    co=0
    for i in val:
        ro=1
        for j in col:
            if j[0]==i:
                for k in j[1:]:
                    ans[ro][co]=k
                    ro+=1
        co+=1
    print('\n'.join([' '.join([str(i) for i in j]) for j in ans]))
          
            
    
    
for _ in range(inp()):
    solve()
