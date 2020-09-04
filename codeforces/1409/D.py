def su(n):
    return sum(list(map(int,str(n))))
for _ in range(int(input())):

    n,m=map(int,input().split())
    s=su(n)
    if s<=m:
        print(0)
    else:
        c=1
        a=n
        while su(n)>m:
            c*=10
            n//=10
            n+=1

        print(n*c - a)
