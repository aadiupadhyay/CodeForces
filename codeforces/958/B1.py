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
    ans=0
    d={}
    for i in range(n-1):
        a,b=mp()
        d[a]=d.get(a,[])+[b]
        d[b]=d.get(b,[])+[a]
    #pr(d)
    for i in d:
        if len(d[i])==1:
            ans+=1
    pr(ans)
    
for _ in range(1):
    solve()
