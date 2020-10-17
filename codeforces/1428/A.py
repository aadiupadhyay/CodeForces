    
from sys  import stdin,stdout

st=lambda:list(stdin.readline().strip())
li=lambda:list(map(int,stdin.readline().split()))
mp=lambda:map(int,stdin.readline().split())
inp=lambda:int(stdin.readline())
pr=lambda n: stdout.write(str(n)+"\n")

mod=1000000007

def solve():
    a,b,c,d= mp()
    if b==d:
        pr(abs(a-c))
        return
    if a==c:
        pr(abs(b-d))
        return
    pr(abs(a-c)+abs(b-d)+2)
    
    
for _ in range(inp()):
    solve()
