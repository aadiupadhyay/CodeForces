def solve():
    n=int(input())
    l=list(map(int,input().split()))
    x=0
    c=0
    d={25:0,50:0,100:0}
    for i in l:
        z=i-25
        if z!=0:
            if z==25:
                if d[z]>=1:
                    d[z]-=1
                else:
                    c=1
                    break
            elif z==75:
                if d[50]>=1 and d[25]>=1:
                    d[50]-=1
                    d[25]-=1
                elif d[25]>=3:
                    d[25]-=3
                else:
                    c=1
                    break
        d[i]+=1
            
        
    if c==0:
        print("YES")
    else:
        print("NO")
        

solve()