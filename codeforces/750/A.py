k,r=map(int,input().split())
c=0
x=240-r
for i in range(1,k+1):
    if x-(5*i)>=0:
        x-=5*i
        c+=1
    else:
        break
    
print(c)
