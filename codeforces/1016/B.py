from sys  import stdin,stdout
from math import gcd
st=lambda:list(stdin.readline().strip())
li=lambda:list(map(int,stdin.readline().split()))
mp=lambda:map(int,stdin.readline().split())
inp=lambda:int(stdin.readline())
pr=lambda n: stdout.write(str(n)+"\n")

def solve():
    a,b,q=mp()
    s=input()
    t=input()
    dp=[0]
    for i in range(a-b+1):
        if s[i:i+b]==t:
            dp.append(dp[-1]+1)
        else:
            dp.append(dp[-1])

    for i in range(len(dp),a+1):
        dp.append(dp[-1])

    for i in range(q):
        x,y=mp()
        x-=1
        y-=b-1
        if x<y:
            pr(dp[y]-dp[x])
        else:
            pr(0)
            
for _ in range(1):
    solve()

