
from math import gcd,ceil,floor,sqrt
 
 
def solve():
    n=int(input())
    l=list(map(int,input().split()))
    l.sort()
    x=l[-1]
    a=n-1
    c=1
    b=1
    prev=1
    while b<x:
        prev=c
        c+=1
        b=pow(c,a)
    ans1=0
    ans2=0
    for i in range(n):
        ans1+=abs(l[i]-pow(prev,i))
        ans2+=abs(l[i]-pow(c,i))
    print(min(ans1,ans2))
        
        
 
 
for _ in range(1):
    solve()
 