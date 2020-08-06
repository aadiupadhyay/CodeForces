n,m=map(int,input().split())
a=set(map(int,input().split()))
b=set(map(int,input().split()))
if a&b:
    print(min(a&b))
else:
    x=min(a)
    y=min(b)
    print(min(x,y)*10+max(x,y))