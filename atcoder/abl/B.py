from sys  import stdin,stdout

from collections import Counter

st=lambda:list(stdin.readline().strip())
li=lambda:list(map(int,stdin.readline().split()))
mp=lambda:map(int,stdin.readline().split())
inp=lambda:int(stdin.readline())
pr=lambda n: stdout.write(str(n)+"\n")

from bisect import bisect_left,bisect_right

mod=1000000007
INF=float('inf')

def solve():
    '''
    n=inp()
    a,b=mp()
    z=n-min(a,b)
    p=min(a,b)-1
    print(max(z*z, p*p))
   
    s=st()
    d=Counter(s)
    l=[]
    l=list(d.values())
    if max(l)==min(l):
        pr(0)
    else:
    '''
    a,b,x,y=mp()
    if a in range(x,y+1) or b in range(x,y+1) :
        pr('Yes')
    elif x in range(a,b+1) or y in range(a,b+1):
        pr('Yes')
    else:
        pr('No')
for _ in range(1):

    solve()
