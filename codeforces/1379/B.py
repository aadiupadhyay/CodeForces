from sys  import stdin,stdout

st=lambda:list(stdin.readline().strip())
li=lambda:list(map(int,stdin.readline().split()))
mp=lambda:map(int,stdin.readline().split())
inp=lambda:int(stdin.readline())
pr=lambda n: stdout.write(str(n)+"\n")

def solve():
    l,r,m=mp()
    d=r-l
 
    for a in range(l,r+1):
        
        rem=m%a
        #print(a,rem)
        
        if(rem<=d):
            c=l
            b=l+rem
            if(m!=b-c):
                break
        
        rem=a-rem
        if(rem<=d):
            b=l
            c=l+rem
            if(m!=b-c):
                break
 
    print(a,b,c)
            
        
        



for _ in range(inp()):
    solve()
    
