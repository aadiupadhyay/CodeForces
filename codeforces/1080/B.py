for _ in range(int(input())):
    a,b=map(int,input().split())
    c=(b*(b+1))//2
    x=(b- (b//2))
    v=(a-(a//2))
    summ=x*x -v*v
    even=a
    if a&1:
        summ+=a
        even=a+1
    n=b//2 - a//2
    if a%2==0:
        n+=1
        
    s=(n)*(even +(n-1))
    
    print(s-summ)
 
