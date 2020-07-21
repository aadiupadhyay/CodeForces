n,k=map(int,input().split())
ma=float("-inf")
for _ in range(n):
    a,b=map(int,input().split())
    if b>k:
        x=a-b+k
    else:
        x=a
    if x>ma:
        ma=x
print(ma)
    
    
