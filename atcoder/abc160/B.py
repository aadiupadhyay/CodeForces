from sys  import stdin,stdout

st=lambda:list(stdin.readline().strip())
li=lambda:list(map(int,stdin.readline().split()))
mp=lambda:map(int,stdin.readline().split())
inp=lambda:int(stdin.readline())
pr=lambda n: stdout.write(str(n)+"\n")

mod=1000000007

def solve():
    n=inp()
    ans= 1000* (n//500)
    n-= 500*(n//500)
    ans+= 5*(n//5)
    pr(ans)
                
        
    
for _ in range(1):
    solve()
