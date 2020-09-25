from sys  import stdin,stdout
from  collections import Counter
st=lambda:list(stdin.readline().strip())
li=lambda:list(map(int,stdin.readline().split()))
mp=lambda:map(int,stdin.readline().split())
inp=lambda:int(stdin.readline())
pr=lambda n: stdout.write(str(n)+"\n")


n=inp()
l=li()
k=li()
v=[False for i in range(n)]
d={l[i]:i for i in range(n)}

for i in k:
    ans=0
    x=d[i]
    if v[x]:
        print(0,end=' ')
    else:
        while x>=0 and not v[x]:
            ans+=1
            v[x]=True
            x-=1
        print(ans,end=' ')

