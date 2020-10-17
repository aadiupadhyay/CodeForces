    
from sys  import stdin,stdout

st=lambda:list(stdin.readline().strip())
li=lambda:list(map(int,stdin.readline().split()))
mp=lambda:map(int,stdin.readline().split())
inp=lambda:int(stdin.readline())
pr=lambda n: stdout.write(str(n)+"\n")

mod=1000000007

def solve():
    s=st()
    l=[]
    n=len(s)
    for i in range(n):
        if l:
            
            if l[-1]=='A' and s[i]=='B':
                l.pop()
                
            elif l[-1]=='B' and s[i]=='B':
                l.pop()
                
            else:
                l.append(s[i])
            
        else:
            l.append(s[i])

    pr(len(l))
    
for _ in range(inp()):
    solve()
