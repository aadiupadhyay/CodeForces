n=int(input())
l=list(map(int,input().split()))
d={}
for i in l:
    d[i]=d.get(i,0)+1
s=0
for i in d:
    if i!=0 and -i in d:
        s+=d[i]*d[-i]
        d[i]=0
        d[-i]=0
if 0 in d:
    for i in range(d[0]):
        s+=i
print(s)
