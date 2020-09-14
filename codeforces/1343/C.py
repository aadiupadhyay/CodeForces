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
    i=0
    ans=[]
    while i<n:
        j=i+1
        x=[l[i]]
        if l[i]<0:
            while j<n and l[j]<0:
                x.append(l[j])
                j+=1
        else:
            while j<n and l[j]>0:
                x.append(l[j])
                j+=1
        ans.append(x)
        i=j
    val=0
    for i in ans:
        val+=max(i)
    print(val)
                


for _ in range(inp()):
    solve()
