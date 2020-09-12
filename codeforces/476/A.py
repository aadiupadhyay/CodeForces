from sys  import stdin,stdout

li=lambda:list(map(int,stdin.readline().split()))
mp=lambda:map(int,stdin.readline().split())
inp=lambda:int(stdin.readline())
pr=lambda n: stdout.write(str(n)+"\n")

def solve():
    n,m=mp()
    a=n>>1
    c=0
    b=n%2
    for i in range(a+1):
        if (a+b)%m==0:
            pr(a+b)
            return 
        a-=1
        b+=2
    pr(-1)
 
 
 
for _ in range(1):
    solve()
