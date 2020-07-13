for _ in range(int(input())):

    n=int(input())
    c=0
    l=list(map(int,input().split()))
    for i in range(1,n-1):
        if l[i]>l[i-1] and l[i]>l[i+1]:
            print("YES")
            print(i,i+1,i+2)
            c=1
            break
    if c==0:
        print("NO")

            
        
        
        
