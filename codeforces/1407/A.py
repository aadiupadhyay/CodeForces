for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    a=l.count(0)
    b=n-a
    if a>=b:
        print(a)
        print('0 '*a)
    else:
        if b&1:
            b-=1
        print(b)
        print('1 '*b)
