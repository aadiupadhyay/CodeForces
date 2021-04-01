for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    s=sum(l)
    if s==n and n%2:
        print("First")
    elif s==n and n%2==0:
        print("Second")
    else:
        w=0
        for i in l:
            if i==1:
                w=1-w
            else:
                break
        if w==0:
            print("First")
        else:
            print("Second")
