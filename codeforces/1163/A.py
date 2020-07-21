n,m=map(int,input().split())
if n==m:
    print(0)
elif m==0:
    print(1)
else:
    print(min(n-m,m))
