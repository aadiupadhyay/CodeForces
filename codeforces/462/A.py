n=int(input())
l=[]
flag=False
for  i in range(n):
    s=input()
    l.append(list(s))
for i in range(n):
    for j in range(n):
        
        c=0
        if i-1>=0 and l[i-1][j]=='o':
            c+=1
        if i+1<n and l[i+1][j]=='o':
            c+=1
        if j-1>=0 and l[i][j-1]=='o':
            c+=1
        if j+1<n and l[i][j+1]=='o':
            c+=1

        if c&1:
            flag=True
            break
    
if flag:
    print('NO')

else:
    print('YES')


    
