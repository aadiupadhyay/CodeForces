n,m=map(int,input().split())
d={i:[] for i in range(1,n+1)}
for _ in range(m):
    a,b=map(int,input().split())
    d[a].append(b)
    d[b].append(a)
c=0
one,two=0,0
star=0
for i in d:
    if len(d[i])==1:
        c+=1
        one+=1
    elif len(d[i])==2:
        two+=1
    elif len(d[i])==n-1:
        star+=1
       
if c==(n-1) and star==1:
    print('star topology')

elif one==2 and  two==(n-2):
    print('bus topology')

elif two==n:
    print('ring topology')
else:
    print('unknown topology')

