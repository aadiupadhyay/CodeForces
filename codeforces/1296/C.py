from sys  import stdin,stdout
from collections import deque
st=lambda:list(stdin.readline().strip())
li=lambda:list(map(int,stdin.readline().split()))
mp=lambda:map(int,stdin.readline().split())
inp=lambda:int(stdin.readline())
pr=lambda n: stdout.write(str(n)+"\n")

mod=1000000007
INF=float('inf')


def solve():
    MIN=INF
    d={(0,0):0}
    n=inp()
    s=['Z']+st()
    x,y=0,0
    X_cor,Y_cor=-1,-1
    for i in range(1,n+1):
        if s[i]=='L':
            x-=1
        if s[i]=='R':
            x+=1
        if s[i]=='D':
            y-=1
        if s[i]=='U':
            y+=1
        
        if (x,y) in d:

            A= d[(x,y)]
            if i-A< MIN:
                X_cor=A+1
                Y_cor=i
                MIN= i-A
                d[(x,y)]=i
            else:
                d[(x,y)]=i
                
        else:
            d[(x,y)]=i

     
    if MIN!=INF:
        print(X_cor,Y_cor)
    else:
        print(-1)
                
                
    

for _ in range(inp()):

    solve()
    
    
    
                
        

