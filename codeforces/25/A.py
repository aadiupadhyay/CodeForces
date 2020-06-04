n=int(input())
l=list(map(int,input().split()))
a=[]
b=[]
for i in range(n):
    if l[i]&1:
        a.append(i+1)
    else:
        b.append(i+1)
if len(a)==1:
    print(a[0])
else:
    print(b[0])
        
