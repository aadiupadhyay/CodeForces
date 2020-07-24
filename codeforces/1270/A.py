for _ in range(int(input())):
    a,b,c=map(int,input().split())
    s=set(map(int,input().split()))
    d=set(map(int,input().split()))
    if a in s:
        print("YES")
    else:
        print("NO")
