from sys  import stdin,stdout

st=lambda:list(stdin.readline().strip())
li=lambda:list(map(int,stdin.readline().split()))
mp=lambda:map(int,stdin.readline().split())
inp=lambda:int(stdin.readline())
pr=lambda n: stdout.write(str(n)+"\n")

mod=1000000007
INF=float('inf')

def solve():
    n=inp()
    s=inp()
    s=str(s)
    odd,even=0,0
    for i in range(1,n+1):
        if i&1 and int(s[i-1])&1:
            odd+=1
        if i%2==0 and int(s[i-1])%2==0:
            even+=1
    if n&1:
        if odd:
            pr(1)
        else:
            pr(2)
    else:
        if even:
            pr(2)
        else:
            pr(1)
        
    


for _ in range(inp()):
    solve()
