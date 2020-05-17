import math
for _ in range(int(input())):
    a,b,c,d=map(int,input().split())
    if a<=b:
        print(b)
    else:
        if c<=d:
            print("-1")
        else:
            x=a-b
            y=c-d
            z=math.ceil(x/y)
            print(z*c+b)
        
            
            
