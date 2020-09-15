from sys  import stdin,stdout
from collections import deque
st=lambda:list(stdin.readline().strip())
li=lambda:list(map(int,stdin.readline().split()))
mp=lambda:map(int,stdin.readline().split())
inp=lambda:int(stdin.readline())
pr=lambda n: stdout.write(str(n)+"\n")

mod=1000000007
def solve():
    n,v=mp()
    ans=[]
    for i in range(1,n+1):
        l=li()
        if min(l[1:])<v:
            ans.append(i)
    print(len(ans))
    print(*sorted(ans))
        

for _ in range(1):
    solve()
