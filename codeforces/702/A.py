n=int(input())
l=list(map(int,input().split()))
k=[1]*n
i=0
while i<1:
    x=i
    j=i+1
    while j<n:
        if l[x]>=l[j]:
            break
        else:
            k[i]+=1
        j+=1
        x+=1
    i+=1
i=1
while i<n-1:
    if l[i]>l[i-1]:
        if k[i-1]!=1:
            k[i]=k[i-1]-1
        else:
            x=i
            j=i+1
            while j<n:
                if l[j]>l[j-1]:
                    k[x]+=1
                else:
                    break
                j+=1
    else:
        
        x=i
        j=i+1
        while j<n:
            if l[j]>l[j-1]:
                k[x]+=1
            else:
                break
            j+=1
    i+=1

print(max(k))
