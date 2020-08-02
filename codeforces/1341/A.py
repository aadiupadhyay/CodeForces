for _ in range(int(input())):
    n,a,b,c,d=map(int,input().split())
    if (a+b)*n<c-d or c+d<(a-b)*n:
        print("No")
    else:
        print("Yes")