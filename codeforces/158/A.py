n,k=map(int,input().split())
l=list(map(int,input().split()))
z=l[k-1]
c=0
for i in l:
    if i>0 and i>=z:
        c+=1
print(c)