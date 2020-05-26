for _ in range(int(input())):
    n=int(input())
    li= list(map(int,input().split()))
    li.sort()
    c=1
    ans=1
    x=0
    f=0
    while(x<n):
        if(li[x]<=c):
            f=1
            ans=c
        c+=1
        x+=1
    if(f==0):
        print(ans)
    else:
        print(ans+1)
    