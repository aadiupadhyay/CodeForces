import bisect
def soe():
    n=1000000
    i=2
    prime=[True]*(n+1)
    while i*i<=n:
        if prime[i]:
            for j in range(i*i,n+1,i):
                prime[j]=False
        i+=1
    l=[]
    i=2
    while i<=n:
        if prime[i]:
            l.append(i*i)
        i+=1
    return l

x=soe()
n=int(input())
l=list(map(int,input().split()))
for i in l:
    a=bisect.bisect_left(x,i)
   
    if a==len(x):
        a-=1
    if x[a]==i:
        print("YES")
    else:
        print("NO")
