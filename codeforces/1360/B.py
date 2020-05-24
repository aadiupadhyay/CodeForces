for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    l.sort()
    k=[]
    for i in range(1,n):
        k.append(l[i]-l[i-1])
    print(min(k))
