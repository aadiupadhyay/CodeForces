n=int(input())

l=list(map(int,input().split()))

s=sum(l)
d={}
for i in l:
    d[i]=d.get(i,0)+1

for i in range(int(input())):

    a,b=map(int,input().split())
    if a not in d:
        print(s)
        continue
    
    x=d[a]
    d[a]-=x
    d[b]=d.get(b,0)+x
    s-=x*a
    s+=x*b
    print(s)
