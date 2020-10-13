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

    n,k=mp()
    l=li()
    ans=0
    for i in range(k):
        x=[]    
        for j in range(i,n,k):
            x.append(l[j])
        a=x.count(1)
        b=len(x)-a
        ans+= min(a,b)
    pr(ans)
            
for _ in range(1):

    solve()
