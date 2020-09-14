from sys  import stdin,stdout
from collections import Counter
st=lambda:list(stdin.readline().strip())
li=lambda:list(map(int,stdin.readline().split()))
mp=lambda:map(int,stdin.readline().split())
inp=lambda:int(stdin.readline())
pr=lambda n: stdout.write(str(n)+"\n")

mod=1000000007
def solve():
    n=inp()
    ans=0
    for i in range(1,n+1):
        ans+=pow(2,i)
    pr(ans)


for _ in range(1):
    solve()
