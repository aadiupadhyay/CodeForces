from sys  import stdin,stdout
from math import ceil
st=lambda:list(stdin.readline().strip())
li=lambda:list(map(int,stdin.readline().split()))
mp=lambda:map(int,stdin.readline().split())
inp=lambda:int(stdin.readline())
pr=lambda n: stdout.write(str(n)+"\n")

mod=1000000007

def solve():
    n=inp()
    l=li()
    ans=[]
    c=0
    d=0
    for i in range(n):
        if l[i]<0:
            if c==2:
                ans.append(d)
                c=1
                d=0
            else:
                c+=1
                
        d+=1
    if d:
        ans.append(d)
    pr(len(ans))
    print(*ans)
        
            
    
        
    
for _ in range(1):
    solve()
