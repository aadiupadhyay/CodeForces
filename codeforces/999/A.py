n,k=map(int,input().split())
l=list(map(int,input().split()))
i,c=0,0
while i<n:
    if l[i]<=k:
        i+=1
        c+=1
    else:
        break

j=n-1
while j>i:
    if l[j]<=k:
        j-=1
        c+=1
    else:
        break
print(c)
