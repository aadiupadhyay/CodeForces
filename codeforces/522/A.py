d={'polycarp':[]}
for _ in range(int(input())):

    s=input().lower().split()
    name1,name2=s[0],s[2]

    d[name2].append(name1)
    d[name1]=[]

stack=['polycarp']
visited={'polycarp'}
level={'polycarp':1}
while stack:
    a=stack.pop()
    for i in d[a]:
        if i not in visited:
            visited.add(i)
            stack.append(i)
            level[i]=level[a]+1

print(max(list(level.values())))
        
