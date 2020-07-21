n=int(input())
l=list(map(int,input().split()))
l=l+l
x=[0]*(2*n)
if l[0]:
    x[0]=1
    
for i in range(1,2*n):
    if l[i]:
        if l[i-1]:
            x[i]=x[i-1]+1
        else:
            x[i]=1
print(max(x))
        
        
