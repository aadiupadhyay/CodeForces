from sys  import stdin,stdout
from math import ceil
st=lambda:list(stdin.readline().strip())
li=lambda:list(map(int,stdin.readline().split()))
mp=lambda:map(int,stdin.readline().split())
inp=lambda:int(stdin.readline())
pr=lambda n: stdout.write(str(n)+"\n")

mod=1000000007

def solve():
    a,b=mp()
    ans=0
    for i in range(a,b+1):
        x=str(i)
        if x==x[::-1]:
            ans+=1
    pr(ans)
for _ in range(1):
    solve()
