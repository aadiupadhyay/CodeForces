n=int(input())
l=list(map(int,input().split()))
mi,ma=l[0],l[0]
c=0
for i in range(1,n):
    if l[i]<mi:
        mi=l[i]
        c+=1
    if l[i]>ma:
        ma=l[i]
        c+=1
print(c)
