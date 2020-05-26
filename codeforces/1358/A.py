for _ in range(int(input())):
    a,b=map(int,input().split())
    z=a*b
    if z&1:
        print(z//2+1)
    else:
        print(z//2)
