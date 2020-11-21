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
    n,k = mp()
    a=st()
    b=st()
    x,y=[],[]
    d={chr(i):0 for i in range(97,123)}
    for i in a:
        d[i]+=1
    for i in b:
        d[i]-=1
    for i in d:
        if d[i]%k:
            pr('NO')
            return 
        if d[i]>0:
            while d[i]>0:
                d[i]-=k
                x.append(i)
        elif d[i]<0:
            while d[i]<0:
                d[i]+=k
                y.append(i)
    x.sort()
    y.sort()
    if len(x)!=len(y):
        pr('NO')
        return 
    for i in range(len(x)):
        if x[i]>y[i]:
            pr('NO')
            return 
    pr('YES')
        
            
    
for _ in range(inp()):
    solve()
