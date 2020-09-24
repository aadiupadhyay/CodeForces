from sys  import stdin,stdout

st=lambda:list(stdin.readline().strip())
li=lambda:list(map(int,stdin.readline().split()))
mp=lambda:map(int,stdin.readline().split())
inp=lambda:int(stdin.readline())
pr=lambda n: stdout.write(str(n)+"\n")
from  math import floor
mod=1000000007
INF= float('inf')
def solve():
    n=inp()
    l=li()
    i=0
    l.sort()
    while i<n:
        f=0
        for j in range(n):
            if i==j:
                continue
            if l[j]>l[i]:
                l[j]-= l[i]*((l[j]-1)//l[i])
                f=1
        l.sort()
        if f==0:
            i+=1
    pr(sum(l))
  
for _ in range(1):
    solve()
