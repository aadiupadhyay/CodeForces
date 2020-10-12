from sys  import stdin,stdout
from math import ceil
st=lambda:list(stdin.readline().strip())
li=lambda:list(map(int,stdin.readline().split()))
mp=lambda:map(int,stdin.readline().split())
inp=lambda:int(stdin.readline())
pr=lambda n: stdout.write(str(n)+"\n")

mod=1000000007
INF=float('inf')

def solve():
    n,v,l,r=mp()
    t= n//v
    a= r//v
    b= l//v
    x= a-b
    
    if l%v==0:
        x+=1
    #print('x',x)
    pr(t-x)
 
        
            
for _ in range(inp()):

    solve()
