for _ in range(int(input())):
    c,x=0,0
    n=int(input())
    for i in range(1,10):
        x=x*10+1
        for j in range(1,10):
            if x*j<=n:
                c+=1
    print(c)
            
            
