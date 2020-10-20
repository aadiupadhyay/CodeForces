from sys  import stdin,stdout
from collections import *

st=lambda:list(stdin.readline().strip())
li=lambda:list(map(int,stdin.readline().split()))
mp=lambda:map(int,stdin.readline().split())
inp=lambda:int(stdin.readline())
pr=lambda n: stdout.write(str(n)+"\n")

mod=1000000007
INF= float('inf')

l=[]
for i in range(1,10):
    l.append(str(i))
    l.append(2*str(i))
    l.append(3*str(i))
    l.append(4*str(i))

def solve():
    n=input()
    n=str(n)
    a=l.index(n)
    
    c=1
    ans=0
    for i in range(a+1):
        ans+=len(l[i])
    print(ans)
        
        
    
    
    
        

for _ in range(inp()):

    solve()

