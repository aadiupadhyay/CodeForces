m=int(input())
l=list(map(int,input().split()))
p,n,z=[],[],[]
for i in range(m):
    if l[i]>0:
        p.append(l[i])
    elif l[i]<0:
        n.append(l[i])
    else:
        z.append(l[i])
if not p:
    p=n[:2]
    n=n[2:]
print(1,n[0])
print(len(p),*p)
print(len(z)+len(n)-1,*z,*n[1:])

    


            
        
