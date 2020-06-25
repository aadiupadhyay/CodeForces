n=int(input())
l=[100,20,10,5,1]
i=0
c=0
while n!=0:
    c+=n//l[i]
    n=n%l[i]
    i+=1
print(c)
    
