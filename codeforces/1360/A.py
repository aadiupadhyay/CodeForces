for _ in range(int(input())):
    a,b=map(int,input().split())
    z=min(a,b)
    z=z*2
    x=max(max(a,b),z)
    print(x*x)
