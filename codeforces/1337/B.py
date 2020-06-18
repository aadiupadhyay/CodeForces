def solve():

    x,n,m=map(int,input().split())
    while x>0 and n!=0 and x>(x//2)+10:
        x=x//2+10
        n-=1
        
    if x>m*10:
        print("NO")
    else:
        print("YES")
for _ in range(int(input())):
    solve()
