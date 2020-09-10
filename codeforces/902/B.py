from collections import deque
n=int(input())
l=list(map(int,input().split()))
k=list(map(int,input().split()))
col_dict={i+1:k[i] for i in range(n)}
d={i:[] for i in range(1,n+1)}
c=2

for i in l:
    d[i].append(c)
   
    c+=1
col=[0 for i in range(n+1)]
q=deque()
q.append(1)
ans=0
while q:
    a=q.popleft()
    if col[a]==col_dict[a]:
        for i in d[a]:
            q.append(i)
        continue
    color=col_dict[a]
    col[a]=color
    stack=[a]
    while stack:
        z=stack.pop()
        for i in d[z]:
            col[i]=color
            stack.append(i)
    for i in d[a]:
        q.append(i)
    
    ans+=1
    
print(ans)  
    
    
