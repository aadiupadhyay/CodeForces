s,n=map(int,input().split())
flag=0
l=[]
for i in range(n):
    a,b=map(int,input().split())
    l.append([a,b])
l.sort()
for i in l:
    if s<=i[0]:
        flag=1
    else:
        s+=i[1]
if flag:
    print('NO')
else:
    print('YES')

