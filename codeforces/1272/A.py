def solve(a,b,c):
    return abs(a-b)+abs(b-c)+abs(c-a)

for _ in range(int(input())):
    x=[]
    a,b,c=list(map(int,input().split()))
    mi=100000000000
    for i in range(-1,2):
        for j in range(-1,2):
            for k in range(-1,2):
                x=a+i
                y=b+j
                z=c+k
                mi=min(mi,solve(x,y,z))
    print(mi)

    
    
            
