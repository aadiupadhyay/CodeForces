l=list(map(int,input().split()))
l.sort()
a=(l[0]-l[1]+l[2])//2
b=l[0]-a
c=l[-1]-a-b
print(a,b,c)
