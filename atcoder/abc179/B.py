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
    f=0
    ans=0
    for i in range(n):
        a,b=mp()
        if a==b:
            ans+=1
        else:
            ans=0
        if ans==3:
            f=1
            break
    if f:
        pr('Yes')
    else:
        pr('No')
            
        
