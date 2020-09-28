from sys  import stdin,stdout
from math import ceil
st=lambda:list(stdin.readline().strip())
li=lambda:list(map(int,stdin.readline().split()))
mp=lambda:map(int,stdin.readline().split())
inp=lambda:int(stdin.readline())
pr=lambda n: stdout.write(str(n)+"\n")

mod=1000000007

def solve():
    n=inp()
    a=n//2
    if a&1:
        pr('NO')
    else:
        val=10**8
        a=[val]
        eve=val
        for i in range(1,n//2):
            eve+=2*i
            a.append(2*i)
        odd=0
        for i in range(1,n//2):
            odd+=2*i -1
            a.append(2*i -1 )
        a.append(eve - odd)
        print('YES')
        print(*a)
            
            
    
for _ in range(inp()):
    solve()
