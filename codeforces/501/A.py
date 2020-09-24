from sys  import stdin,stdout

st=lambda:list(stdin.readline().strip())
li=lambda:list(map(int,stdin.readline().split()))
mp=lambda:map(int,stdin.readline().split())
inp=lambda:int(stdin.readline())
pr=lambda n: stdout.write(str(n)+"\n")

mod=1000000007

def solve():
    a,b,c,d=mp()
    m=max((3*a)//10 , a- ((a*c)//250))
    v=max((3*b)//10 , b- ((b*d)//250))
    if v==m:
        pr('Tie')
    elif v>m:
        pr('Vasya')
    else:
        pr('Misha')


for _ in range(1):
    solve()
