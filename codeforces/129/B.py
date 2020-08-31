
n,m=map(int,input().split())
d={i:set() for i in range(1,n+1)}
for i in range(m):
    a,b=map(int,input().split())
    d[a].add(b)
    d[b].add(a)
    
c=1
grp=0
while True:
    flag=0
    ans=[]
    for i in d:
        if len(d[i])==1:
            flag=1
            d[i]=set()
            ans.append(i)

    if flag:
        for i in ans:
            for j in d:
                if i in d[j]:
                    d[j].discard(i)
    else:
        break

    grp+=1


print(grp)
            
