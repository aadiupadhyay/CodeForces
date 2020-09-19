from sys  import stdin,stdout

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
    l.sort()
    i=0
    j=n-1
    k=[]
    for x in range(n):
        if x&1:
            k.append(l[i])
            i+=1
        else:
            k.append(l[j])
            j-=1
    ans=0
    for i in range(1,n-1,2):
        if k[i]<k[i-1] and k[i]<k[i+1]:
            ans+=1
    pr(ans)
    print(*k)
        
    


for _ in range(1):
    solve()
