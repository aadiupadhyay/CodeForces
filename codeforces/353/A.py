from sys  import stdin,stdout

st=lambda:list(stdin.readline().strip())
li=lambda:list(map(int,stdin.readline().split()))
mp=lambda:map(int,stdin.readline().split())
inp=lambda:int(stdin.readline())
pr=lambda n: stdout.write(str(n)+"\n")

mod=1000000007
INF= float('inf')
def solve():
    n=inp()
    x,y,c=0,0,0
    for i in range(n):
        a,b=mp()
        x+=a
        y+=b
        if a%2!=b%2:
            c+=1
    if x%2==0 and y%2==0:
        pr(0)
        return
    if x%2!=y%2:
        pr(-1)
        return
    pr(1 if c else -1)
  
for _ in range(1):
    solve()
