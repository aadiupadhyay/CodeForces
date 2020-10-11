from sys  import stdin,stdout
from bisect import bisect_left
st=lambda:list(stdin.readline().strip())
li=lambda:list(map(int,stdin.readline().split()))
mp=lambda:map(int,stdin.readline().split())
inp=lambda:int(stdin.readline())
pr=lambda n: stdout.write(str(n)+"\n")

mod=1000000007
INF=float('inf')

def solve():
    l=li()
    if sum(l)%2==0:
        l.sort()
        for i in range(4):
            for j in range(4):
                if i!=j:

                    s=l[i]+l[j]
                    v=0
                    for k in range(4):
                        if k==i or k==j:
                            continue
                        v+=l[k]
                        
                    #print(s,v)
                    if s==v:
                        pr('Yes')
                        return
        for i in l:
            if sum(l)- i == i:
                pr('Yes')
                return 
        pr('No')
                            
    else:
        pr('No')



for _ in range(1):

    solve()
