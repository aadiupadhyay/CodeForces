def solve():
    n=int(input())
    l=list(map(int,input().split()))
    left=[0]*(3002)
    ans=0
    for i in range(n):
        right=[0]*(3002)
        
        for j in range(n-1,i,-1):
            
            ans+=right[l[i]]*left[l[j]]
            right[l[j]]+=1
        left[l[i]]+=1
    print(ans)
 
    
for _ in range(int(input())):
    solve()