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
    l=li()
    d=Counter(l)
    for i in d:
        if d[i]>2:
            pr('NO')
            return
    l.sort()
    x=[]
    y=[]
    for i in range(n):
        if i&1:
            x.append(l[i])
        else:
            y.append(l[i])
    print('YES')
    print(len(x))
    print(*x)
    print(len(y))
    print(*y[::-1])

for _ in range(1):
    solve()
