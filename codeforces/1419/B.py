from sys  import stdin,stdout
from bisect import bisect_left
st=lambda:list(stdin.readline().strip())
li=lambda:list(map(int,stdin.readline().split()))
mp=lambda:map(int,stdin.readline().split())
inp=lambda:int(stdin.readline())
pr=lambda n: stdout.write(str(n)+"\n")

mod=1000000007
INF=float('inf')



def solve():
    n=inp()
    ans=0
    i=1
    p=1
    while n>=(i*(i+1))//2:
        n-= i*(i+1)//2
        i+=pow(2,p)
        p+=1
        ans+=1
    pr(ans)
        
    
    


for _ in range(inp()):
    solve()
