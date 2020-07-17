for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    if n==1:
        print("0")
    else:
        l=l[::-1]
        i=1
        while i<n and l[i]>=l[i-1]:
            i+=1
        while i<n and l[i]<=l[i-1]:
            i+=1
        print(n-i)
        
                
    
