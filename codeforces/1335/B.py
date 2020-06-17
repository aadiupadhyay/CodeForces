def solve():
    n,a,b=map(int,input().split())
    x=""
    while len(x)<n:
        for i in range(b):
            x+=chr(97+i)
    print(x[:n])
for _ in range(int(input())):
    solve()
