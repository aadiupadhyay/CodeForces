def solve():
    a,b=map(int,input().split())
    a=min(a,b)
    if a&1:
        print("Akshat")
    else:
        print("Malvika")
solve()
