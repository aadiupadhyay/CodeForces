n=int(input())
#n=10000000
ksum=0
for k in range(1,n+1):
    m=n//k
    ksum+=k*m*(m+1)//2
    
print(ksum)