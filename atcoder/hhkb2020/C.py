from sys  import stdin,stdout
from math import ceil
st=lambda:list(stdin.readline().strip())
li=lambda:list(map(int,stdin.readline().split()))
mp=lambda:map(int,stdin.readline().split())
inp=lambda:int(stdin.readline())
pr=lambda n: stdout.write(str(n)+"\n")

mod=1000000007

def solve():
    n=inp()
    l=li()
    v=[False for i in range(n+1)]
    s=set()
    prev=0
    s.add(prev)
    for i in l:
        if i>prev:
            s.add(i)
            print(prev)
        else:
            #print(i,s)
            s.add(i)
            while prev in s:
                prev+=1
            print(prev)
        


    
for _ in range(1):
    solve()
