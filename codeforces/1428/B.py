    
from sys  import stdin,stdout

st=lambda:list(stdin.readline().strip())
li=lambda:list(map(int,stdin.readline().split()))
mp=lambda:map(int,stdin.readline().split())
inp=lambda:int(stdin.readline())
pr=lambda n: stdout.write(str(n)+"\n")

mod=1000000007

def solve():
    n=inp()
    s=st()
    if ('<' not in s and '>' in s) or ('<' in s and '>' not in s):
        pr(n)
        return
    p=set()
    for i in range(n):
        if s[i]=='-':
            p.add(i)
            p.add((i+1)%n)
    pr(len(p))
        
    
    
for _ in range(inp()):
    solve()
