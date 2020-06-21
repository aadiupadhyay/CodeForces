n,x=map(int,input().split())
c=0
for i in range(1,n+1):

    if x%i==0 and x//i<=n:
        c+=1
print(c)
