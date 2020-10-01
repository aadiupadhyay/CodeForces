from sys  import stdin,stdout

st=lambda:list(stdin.readline().strip())
li=lambda:list(map(int,stdin.readline().split()))
mp=lambda:map(int,stdin.readline().split())
inp=lambda:int(stdin.readline())
pr=lambda n: stdout.write(str(n)+"\n")

def solve():
    n=inp()
    for i in range(-200,200):
        for j in  range(-200,200):
            if pow(i,5) - pow(j,5) == n:
                print(i,j)
                return
solve()
