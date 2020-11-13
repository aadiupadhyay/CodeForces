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
    n,m=mp()
    l=[li() for i in range(n)]
    for i in range(n):
        for j in range(m):
            if (i+j)%2==0:
                if l[i][j]%2:
                    l[i][j]+=1
            else:
                if l[i][j]%2==0:
                    l[i][j]+=1
            
    print('\n'.join([' '.join([str(i) for i in j]) for j in l]))
                
        
        
            
    
for _ in range(inp()):
    solve()
