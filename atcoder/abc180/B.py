from sys  import stdin,stdout
from math import *
from collections import *
st=lambda:list(stdin.readline().strip())
li=lambda:list(map(int,stdin.readline().split()))
mp=lambda:map(int,stdin.readline().split())
inp=lambda:int(stdin.readline())
pr=lambda n: stdout.write(str(n)+"\n")

mod=1000000007

def solve():
    n= inp()
    l=li()
    ans1,ans2 =0,0
    ans3= float('-inf')
    for i in l:
        ans1 += abs(i)
        ans2 += (i*i)
        ans3= max(ans3,abs(i))
    print(ans1)
    print(sqrt(ans2))
    print(ans3)
    
for _ in range(1):
    solve()
