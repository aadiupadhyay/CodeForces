from sys  import stdin,stdout
from collections import Counter
st=lambda:list(stdin.readline().strip())
li=lambda:list(map(int,stdin.readline().split()))
mp=lambda:map(int,stdin.readline().split())
inp=lambda:int(stdin.readline())
pr=lambda n: stdout.write(str(n)+"\n")

mod=1000000007
INF= float('inf')
'''
def solve():
    n,k=mp()
    s=input()
    s=[len(i) for i in s.split('L')]
    pr(s)
'''
def solve():
    n=inp()
    l=li()
    s=sum(l)
    if s==0:
        pr('NO')
        return
    pr('YES')
    l=sorted(l)
    a=0
    for i in l:
        a+=i
        if a==0:
            print(*l[::-1])
            return

    print(*l)
    
        
        
        
    
    
for _ in range(inp()):
    solve()
