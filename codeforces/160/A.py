n=int(input())
l=list(map(int,input().split()))
l.sort()
s=sum(l)
c=1
i=n-2
x=l[n-1]
s=s-l[n-1]
while i>=0:
    if x>s:
        break
    else:
        x=x+l[i]
        s=s-l[i]
        c=c+1
    i=i-1
print(c)
    
