from sys  import stdin,stdout
from collections  import *
from math import gcd,floor,ceil
st=lambda:list(stdin.readline().strip())
li=lambda:list(map(int,stdin.readline().split()))
mp=lambda:map(int,stdin.readline().split())
inp=lambda:int(stdin.readline())
pr=lambda n: stdout.write(str(n)+"\n")

mod=1000000007
INF=float('inf')

def solve():

    n=inp()
    l=li()
    c=Counter(l)
    for i in c:
        if c[i] > n//3:
            pr(-1)
            return 
    ans=[]
    while True:
        if c[1] and c[2] and c[4]:
            ans.append([1,2,4])
            c[1]-=1 
            c[2]-=1 
            c[4]-=1 
        elif c[1] and c[2] and c[6]:
            ans.append([1,2,6])
            c[1]-=1
            c[2]-=1 
            c[6]-=1 
        elif c[1] and c[3] and c[6]:
            ans.append([1,3,6])
            c[1]-=1 
            c[3]-=1 
            c[6]-=1 
        else:
            break 
    #print(c)
    if not sum(c.values()):
        for i in range(len(ans)):
            print(*ans[i])
    else:
        print(-1)
solve()