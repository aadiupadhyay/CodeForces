def solve():
    n=int(input())
    l=list(map(int,input().split()))
    odd={}
    even={}
    oddc,evenc=0,0
    for i in range(len(l)):
 
        if l[i]&1:
            if oddc==0:
                odd[i+1]=0
                oddc=1
            else:
                odd[i+1]=l[i]
        else:
            if evenc==0:
                even[i+1]=0
                evenc=1
            else:
                even[i+1]=l[i]
 
    
    x=list(odd.keys())
    y=list(even.keys())
    
 
    a,b=len(x),len(y)
 
    if a&1:
        x=x[1:]
        y=y[1:]
    else:
        if len(x)>0:
            x=x[2:]
        else:
            y=y[2:]
 
 
    for i in range(0,len(y)-1,2):
        f,g=y[i],y[i+1]
        print(min(f,g),max(f,g))
        
 
    for j in range(0,len(x)-1,2):
        f,g=x[j],x[j+1]
        print(min(f,g),max(f,g))
        
 
        
 
    
for _ in range(int(input())):
 
    solve()
