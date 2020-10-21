
t=int(input())
for f in range(t):
    n,x=map(int,input().split())
    a=list(map(int,input().split()))
    a.sort()
    s=0
    i=0
    while x>-1:
        if i<n:
            if a[i]==s+1:
                s+=1
                i+=1
            else:
                if a[i]>s:
                    x-=1
                    s+=1
                else:
                    i+=1
        else:
            x-=1
            s+=1
    print(s-1)