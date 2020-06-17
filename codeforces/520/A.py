def solve():
    n=int(input())
    s=input().lower()
    s=set(s)
    if len(s)==26:
        print("YES")
    else:
        print("NO")
    

solve()
