k,r=map(int,input().split())
c=1
x=2
z=k
while k%10!=0 and k%10!=r:
    c+=1
    k=z*x
    x+=1
    
print(c)
