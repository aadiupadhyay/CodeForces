from sys  import stdin,stdout
from collections  import *
from math import gcd,floor,ceil
st=lambda:list(stdin.readline().strip())
li=lambda:list(map(int,stdin.readline().split()))
mp=lambda:map(int,stdin.readline().split())
inp=lambda:int(stdin.readline())
pr=lambda n: stdout.write(str(n)+"\n")

mod=1000000007
INF=float('inf')

def solve():
    n,q=mp()
    s=st()
    ans=[]
    for i in range(q):
        a,b = mp()
        c=0
        for x in range(a-1):
            if s[x]==s[a-1]:
                c=1
        for x in range(b,n):
            if s[x]==s[b-1]:
                c=1
        #pr('YES' if c else 'NO')
        if c:
            ans.append('YES')
        else:
            ans.append('NO')
    pr('\n'.join(ans))

        
            
    
for _ in range(inp()):
    solve()
