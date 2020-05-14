for _ in range(int(input())):
    n=int(input())
    if n<10:
        print("1")
        print(n)
    else:
        l=[]
        x=0
        while n:
            c=n%10
            if c!=0:
                l.append(c*(10**x))
            x=x+1
            n=n//10
        print(len(l))
        print(*l)
                
            
        
