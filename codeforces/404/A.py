from sys  import stdin,stdout
from collections import deque
st=lambda:list(stdin.readline().strip())
li=lambda:list(map(int,stdin.readline().split()))
mp=lambda:map(int,stdin.readline().split())
inp=lambda:int(stdin.readline())
pr=lambda n: stdout.write(str(n)+"\n")
from random import randint

    
mod=1000000007
def solve():
    x=set()
    n=inp()
    s=set()
    for i in range(n):
        l=st()
        s.add(l[i])
        s.add(l[n-i-1])
        for  j in range(n):
            if j==i or j==n-i-1:
                continue
            x.add(l[j])
    
    if len(x)==1 and len(s)==1:
        if x!=s:
            pr('YES')
        else:
            pr('NO')
    else:
        pr('NO')
            

for _ in range(1):
    solve()
