from sys  import stdin,stdout

st=lambda:list(stdin.readline().strip())
li=lambda:list(map(int,stdin.readline().split()))
mp=lambda:map(int,stdin.readline().split())
inp=lambda:int(stdin.readline())
pr=lambda n: stdout.write(str(n)+"\n")

mod=1000000007

def solve():
    n=inp()
    l=li()
    s=set(l)
    if len(s)!=n:
        x,y=set(),set()
        for i in l:
            if i in x:
                y.add(i)
            else:
                x.add(i)
        for i in range(101):
            if i not in x:
                val=i
                break
        for i in range(101):
            if i not in y:
                vall=i
                break
        pr(val+vall)
    else:
        for i in range(101):
            if i not in s:
                pr(i)
                break
                
            


for _ in range(inp()):
    solve()
