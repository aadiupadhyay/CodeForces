    
from sys  import stdin,stdout

st=lambda:list(stdin.readline().strip())
li=lambda:list(map(int,stdin.readline().split()))
mp=lambda:map(int,stdin.readline().split())
inp=lambda:int(stdin.readline())
pr=lambda n: stdout.write(str(n)+"\n")
        

def solve():
    n= inp()
    ans=0
    val=[]
    l=[ st() for i in range(n)]
    if l[0][1]== l[1][0]:
        x= l[0][1]
        a,b = l[n-1][n-2],l[n-2][n-1]
        if a==x:
            ans+=1
            val.append((n,n-1))
        if b==x:
            ans+=1
            val.append((n-1,n))
        print(ans)
        for i in val:
            print(*i)
        return
    a,b= l[n-1][n-2],l[n-2][n-1]
    x,y= l[0][1],l[1][0]
    if a==b:
        z=a
        if x==a:
            ans+=1
            val.append((1,2))
        else:
            ans+=1
            val.append((2,1))
    else:
        ans+=1
        val.append((1,2))
        x= 1-int(x)
        if int(a)==x:
            ans+=1
            val.append((n,n-1))
        else:
            ans+=1
            val.append((n-1,n))
    print(ans)
    for i in val:
        print(*i)

        
    
    
for _ in range(inp()):
    solve()
