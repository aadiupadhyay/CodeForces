n,m = list(map(int,input().split()))
arr = []
for _ in range(n):
    lang = list(map(int,input().split()))
    lang = lang[1::]
    lang = set(lang)
    f = 0
    for i in range(len(arr)):
        x = arr[i].intersection(lang)
        if x!=set():
            arr[i].update(lang)
            f = 1
            break
    if f==0:
        arr.append(lang)
ans = []
visited = [False for i in range(len(arr))]
for i in range(len(visited)):
    if visited[i]==False:
        visited[i] = True
        y = arr[i]
        for j in range(len(visited)):
            if visited[j]==False:
                x = y.intersection(arr[j])
                if x!=set():
                    visited[j] = True
                    y.update(arr[j])
        ans.append(y)
# print(ans)
cnt = 0
m = 0
for i in ans:
    if i==set():
        cnt+=1
    else:
        m+=1
if m==0:
    print(cnt)
else:
    print(m-1+cnt)