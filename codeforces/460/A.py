n,m=map(int,input().split())
i=1
c=0
while i<n+1:
    if i%m==0:
        n+=1
    c+=1
    i+=1
print(c)
