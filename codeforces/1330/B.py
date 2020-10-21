for i in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    b=[0]+a[:]
    left=[0]*(n+1)
    right=[0]*(n+1)
    ma=1
    d={}
    for i in range(1,n+1):
        if b[i] in d:
            break
        d[b[i]]=1
        ma=max(ma,b[i])
        if ma==i:
            left[i]=1
    b=[0]+a[::-1]
    ma=1
    d={}
    for i in range(1,n+1):
        if b[i] in d:
            break
        d[b[i]]=1
        ma=max(ma,b[i])
        if ma==i:
            right[i]=1
    ans=0
    ind=[]
    for i in range(1,n+1):
        if left[i]*right[n-i]:
            ans+=1
            ind.append(i)
    print(ans)
    for i in ind:
        print(i,n-i)
    # print(ind,left,right)