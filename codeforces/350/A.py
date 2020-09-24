from sys  import stdin,stdout

st=lambda:list(stdin.readline().strip())
li=lambda:list(map(int,stdin.readline().split()))
mp=lambda:map(int,stdin.readline().split())
inp=lambda:int(stdin.readline())
pr=lambda n: stdout.write(str(n)+"\n")

mod=1000000007

def solve():
    n,m=mp()
    l=li()
    b=li()
    j,k=min(l),max(l)
    for i in range(min(b)):
        if k<=i and 2*j<=i:
            pr(i)
            return
    pr(-1)
    
'''
1 50
7
65 52 99 78 71 19 96 72 80 15 50 94 20 35 79 95 44 41 45 53 77 50 74 66 59 96 26 84 27 48 56 84 36 78 89 81 67 34 79 74 99 47 93 92 90 96 72 28 78 66
'''
for _ in range(1):
    solve()
