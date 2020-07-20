n=int(input())
x,c,ma=0,0,0
l=list(map(int,input().split()))
for i in l:
    if i :
        c+=1
    if not i:
        x+=1
        if x>ma:
            ma=x
    elif x>0:
        x-=1
if not ma:
    ma-=1
print(ma+c)
    
        
