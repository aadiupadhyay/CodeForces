for _ in range(int(input())):
    l=list(map(int,input().split()))
    n=l[-1]
    l=l[:-1]
    l.sort()
    n-=2*l[2]-l[1]-l[0]
    if n<0 or n%3!=0:
        print("NO")
    else:
        print("YES")