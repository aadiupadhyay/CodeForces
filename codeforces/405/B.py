from sys  import stdin,stdout
from bisect import bisect_left

st=lambda:list(stdin.readline().strip())
li=lambda:list(map(int,stdin.readline().split()))
mp=lambda:map(int,stdin.readline().split())
inp=lambda:int(stdin.readline())
pr=lambda n: stdout.write(str(n)+"\n")

def solve():
    n=inp()
    s=st()
    L=[i for i in range(n) if s[i]=='L']
    R=[i for i in range(n) if s[i]=='R']
    if not L and not R:
        pr(n)
        return
    if (not L) and R:
        pr(R[0])
        return
    if (not R) and L:
        pr(n-1-L[-1])
        return
    
    ans=0
    for i in R:
        a=bisect_left(L,i)
        if a!=len(L):
            if (L[a] - i) % 2==0 :
                ans+=1
    
    if R[0]<L[0]:
        ans+=R[0]
    if L[-1]>R[-1]:
        ans+= n-1 -L[-1]

    for i in L:
        a=bisect_left(R,i)
        if a!=len(R):
            ans+= R[a]- i-1
    pr(ans)
    
for _ in range(1):
    solve()
