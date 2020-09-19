from sys  import stdin,stdout
 
st=lambda:list(stdin.readline().strip())
li=lambda:list(map(int,stdin.readline().split()))
mp=lambda:map(int,stdin.readline().split())
inp=lambda:int(stdin.readline())
pr=lambda n: stdout.write(str(n)+"\n")
 
mod=1000000007
INF=float('inf')
for _ in range(1):
    n=inp()
    l=li()
    l.sort()
    a=l[:n//2]
    b=l[n//2:]
    k=[]
    x,y=0,0
    for i in range(n):
        if i%2==0:
            k.append(b[x])
            x+=1
        else:
            k.append(a[y])
            y+=1
    ans=0
    for i in range(1,n-1,2):
        if k[i]<k[i-1] and k[i]<k[i+1]:
            ans+=1
    pr(ans)
    print(*k)
        
