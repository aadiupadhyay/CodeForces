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
    n=inp()
    l=[-1 for i in range(2*n)]
    for i in range(2*n):
        s=input().split()
        if len(s)==2:
            l[i]=int(s[1])
    x,y=[],[]
    for i in range(2*n-1,-1,-1):
        if l[i]==-1:
            if not x:
                pr('NO')
                return
            else:
                y.append(x.pop())
        else:
            if x and l[i]>x[-1]:
                pr('NO')
                return
            x.append(l[i])
    print('YES')
    print(*y[::-1])
            
                    
        
        
    
for _ in range(1):
    solve()
