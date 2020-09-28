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
    x=[]
    ans=0
    for i in range(n):
        if x==[]:
            x.append(l[i])
        else:
            if l[i]>0:
                if x[-1]>0:
                    x.append(l[i])
                else:
                    ans+=max(x)
                    x=[l[i]]
                    
            else:
                if x[-1]<0:
                    x.append(l[i])
                else:
                    ans+=max(x)
                    x=[l[i]]
                    
            
    if x:
        if x[-1]<0:
            ans+=max(x)
        else:
            ans+=max(x)
    pr(ans)

            
for _ in range(inp()):
    solve()
