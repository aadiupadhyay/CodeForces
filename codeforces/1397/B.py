from math import floor, ceil
def solve():
    n=int(input())
    l=list(map(int,input().split()))
    l.sort()
    x=l[-1]
    a=n-1
    prev=floor(x**(1/a))
    c=ceil(x**(1/a))
    ans1=0
    ans2=0
    for i in range(n):
        ans1+=abs(l[i]-pow(prev,i))
        ans2+=abs(l[i]-pow(c,i))
    print(min(ans1,ans2))
        
        


for _ in range(1):
    solve()
 