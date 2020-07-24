for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    x=0
    s=0
    for i in l:
        x^=i
        s+=i
    if 2*x==s:
        print(0)
    else:
        print(2)
        print(x,s+x)
