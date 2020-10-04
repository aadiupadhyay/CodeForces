from sys  import stdin,stdout
from heapq import *
st=lambda:list(stdin.readline().strip())
li=lambda:list(map(int,stdin.readline().split()))
mp=lambda:map(int,stdin.readline().split())
inp=lambda:int(stdin.readline())
pr=lambda n: stdout.write(str(n)+"\n")

mod=1000000007
INF=float('inf')

def solve():
    n,m=mp()
    l=[]
    for i in range(n):
        a=li()
        l.append(a)
    last_row= n-1
    half= m//2
    last_col= m-1
    half_= n//2 
    ans=0
    for i in range(half_):
        for j in range(half):

            A= l[i][last_col -j]
            B= l[last_row-i][j]
            C= l[last_row-i][last_col-j]
            D= l[i][j]

            c1,c2,c3,c4= abs(A-B)+abs(C-B)+abs(D-B), abs(B-A)+abs(C-A)+abs(D-A), abs(A-C)+abs(B-C)+abs(D-C), abs(A-D)+abs(B-D)+abs(C-D)
            ans+= min(c1,c2,c3,c4)

    if n&1:
        a= n//2
        for i in range(half):
            ans+= abs(l[a][i]- l[a][last_col-i])
    if m&1:
        a=m//2
    
        for i in range(half_):
            
            ans+= abs(l[i][a]- l[last_row-i][a])
    pr(ans)
        
        
        
        
    
for _ in range(inp()):
    solve()
