from sys  import stdin,stdout
from collections import deque
st=lambda:list(stdin.readline().strip())
li=lambda:list(map(int,stdin.readline().split()))
mp=lambda:map(int,stdin.readline().split())
inp=lambda:int(stdin.readline())
pr=lambda n: stdout.write(str(n)+"\n")
from random import randint

    
mod=1000000007
def solve():
    n,k=mp()
    ans=0
    l=input().split()
    for i in l:
        if i.count('4')+i.count('7')<=k:
            ans+=1
    pr(ans)
    

for _ in range(1):
    solve()
