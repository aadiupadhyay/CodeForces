a,b,n=map(int,input().split())
c=0
if a%b==0:
    print(str(a)+'0'*n)
    
else:
    for i in range(10):
        x=a*10 + i
        if x%b==0:
            a=x
            c=1
            break
    if c:
        print(str(a) + '0'*(n-1))

    else:
        print(-1)
        
