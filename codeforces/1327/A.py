def solve():
    a,k=map(int,input().split())
    if k*k>a:
        print("NO")
    elif a%2==0 and  k%2==0:
        print("YES")
    elif a%2 and k%2:
        print("YES")
    else:
        print("NO")
for _ in range(int(input())):
    solve()
