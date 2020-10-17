    
from sys  import stdin,stdout

st=lambda:list(stdin.readline().strip())
li=lambda:list(map(int,stdin.readline().split()))
mp=lambda:map(int,stdin.readline().split())
inp=lambda:int(stdin.readline())
pr=lambda n: stdout.write(str(n)+"\n")

mod=1000000007

def solve():
    x,y,a,b = mp()
    ans=0
    while x*a<y and x*a<x+b:
        x*=a
        ans+=1
    ans+=(y-x-1)//b
    pr(ans)
        
    

    
for _ in range(1):
    solve()
