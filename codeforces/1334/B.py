from sys  import stdin,stdout
from collections import *
st=lambda:list(stdin.readline().strip())
li=lambda:list(map(int,stdin.readline().split()))
mp=lambda:map(int,stdin.readline().split())
inp=lambda:int(stdin.readline())
pr=lambda n: stdout.write(str(n)+"\n")

mod=1000000007
INF= float('inf')

def solve():
    n,k= mp()
    l=li()
    x=sorted(l,reverse=True)
    
    a=0
    ans=0
    i=0
    while i<n and (a+x[i])/(i+1) >= k:
        a+=x[i]
        ans+=1
        i+=1
        
    print(ans)
    

for _ in range(inp()):

    solve()
