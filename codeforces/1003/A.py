n=int(input())
l=list(map(int,input().split()))
d={}
for i in l:
    d[i]=d.get(i,0)+1
mi=-1000
for i in d:
    if d[i]>mi:
        mi=d[i]
print(mi)
