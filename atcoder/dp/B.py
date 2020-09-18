from sys  import stdin,stdout

st=lambda:list(stdin.readline().strip())
li=lambda:list(map(int,stdin.readline().split()))
mp=lambda:map(int,stdin.readline().split())
inp=lambda:int(stdin.readline())
pr=lambda n: stdout.write(str(n)+"\n")

mod=1000000007
INF=float('inf')

n,k=mp()
l=li()
dp=[INF for i in range(n)]
dp[0]=0

for i in range(n):

    for j in range(i+1,min(i+k+1,n)):

        dp[j]=min(abs(l[i]-l[j])+dp[i],dp[j])

print(dp[-1])

        
