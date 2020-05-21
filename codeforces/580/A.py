n=int(input())
l=list(map(int,input().split()))
k=[]
c=1
for i in range(1,n):
    if l[i]>=l[i-1]:
        c+=1
    else:
        k.append(c)
        c=1
k.append(c)
print(max(k))
    
    
