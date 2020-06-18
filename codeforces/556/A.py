def solve():
    n=int(input())
    s=input()
    a=s.count("1")
    b=n-a
    print(abs(a-b))
solve()
