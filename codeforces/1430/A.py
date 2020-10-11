from sys  import stdin,stdout
from collections import defaultdict
st=lambda:list(stdin.readline().strip())
li=lambda:list(map(int,stdin.readline().split()))
mp=lambda:map(int,stdin.readline().split())
inp=lambda:int(stdin.readline())
pr=lambda n: stdout.write(str(n)+"\n")

mod=1000000007
INF=float('inf')

def solve():
    n=inp()
    if n%3==0:
        print(n//3,0,0)
        return
    if n%5==0:
        print(0,n//5,0)
        return
    if n%7==0:
        print(0,0,n//7)
        return
    
    for i in range(70):
        for j in range(70):
            for k in range(70):
                if (3*i + 5*j + 7*k) == n:
                    print(i,j,k)
                    return
    print(-1)
        

for _ in range(inp()):

    solve()
