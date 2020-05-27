n,k=map(int,input().split())
l=list(map(int,input().split()))
for i in range(n):
    l[i]+=k
c=0
for i in l:
    if i<=5:
        c+=1
if c<3:
    print("0")
else:
    print(c//3)
        
    
