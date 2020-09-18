from sys  import stdin,stdout

st=lambda:list(stdin.readline().strip())
li=lambda:list(map(int,stdin.readline().split()))
mp=lambda:map(int,stdin.readline().split())
inp=lambda:int(stdin.readline())
pr=lambda n: stdout.write(str(n)+"\n")

mod=1000000007
INF=float('inf')

n=inp()
l=li()
dp=[0 for i in range(n)]
dp[1]=abs(l[1]-l[0])

for i in range(2,n):
    dp[i]=min(dp[i-2]+abs(l[i]-l[i-2]),abs(l[i]-l[i-1])+dp[i-1])
print(dp[-1])
