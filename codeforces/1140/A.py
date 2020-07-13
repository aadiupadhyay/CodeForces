
for _ in range(1):
    n=int(input())
    l=list(map(int,input().split()))
    c=0
    l=[0]+l
    i=1
    while i<=n:
        c+=1
        ma=i
        while i<=n and i<=ma:
            ma=max(ma,l[i])
            i+=1
    print(c)
  
    

    
    
            
