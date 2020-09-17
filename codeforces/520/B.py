a,b=map(int,input().split())
c=0
while a!=b:
    if b%2:
        b+=1 
    elif b%2==0:
        if b>a:
            b=b//2 
        else:
            b+=1 
    c+=1 
print(c)
    