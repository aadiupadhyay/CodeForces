n,m,a,b=map(int,input().split())
if m*a<=b:
    print(n*a)
else:
    print((n//m)*b + min((n%m)*a,b))
            
        
