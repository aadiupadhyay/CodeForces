for _ in range(int(input())):

    x,y,a,b=map(int,input().split())
    c=y-x
    v=a+b
    if c%v==0:
        print(c//v)
    else:
        print("-1")
