from sys  import stdin,stdout
from collections  import Counter
st=lambda:list(stdin.readline().strip())
li=lambda:list(map(int,stdin.readline().split()))
mp=lambda:map(int,stdin.readline().split())
inp=lambda:int(stdin.readline())
pr=lambda n: stdout.write(str(n)+"\n")

mod=1000000007
INF=float('inf')

def solve():
    n=inp()
    l=li()
    ans=0
    i=0
    d=Counter(l)
    while i<n:
        j=i+1
        x=l[i]
        while j<n:
            x+=l[j]
            if x in d:
                ans+=d[x]
                d[x]=0
            j+=1
        i+=1
    #print(s)
    pr(ans)

        
            
    
for _ in range(inp()):
    solve()
