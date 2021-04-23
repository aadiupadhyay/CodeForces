def valid(x, y):
    if 0 <= x <= n and 0 <= y <= n and x != y and l[x][y] != -1 and l[x][y] == 0:
        return 1
    return 0


def dfs(i, j, c):
    c = c-1
    stack = [[i, j, c]]
    while stack:
        nodex, nodey, c = stack.pop()
        if c > 0:
            if valid(nodex, nodey-1):
                nodey = nodey-1
                l[nodex][nodey] = l[i][i]
                c = c-1
            elif valid(nodex+1, nodey):
                nodex += 1
                l[nodex][nodey] = l[i][i]
                c = c-1
            elif valid(nodex, nodey+1):
                nodey += 1
                l[nodex][nodey] = l[i][i]
                c = c-1
            else:
                return 0
            stack.append([nodex, nodey, c])
    return 1


n = int(input())
ans = list(map(int, input().split()))
l = [[0 for i in range(n)]for j in range(n)]
for i in range(n):
    l[i][i] = ans[i]
for i in range(n):
    for j in range(i+1, n):
        l[i][j] = -1
for i in range(n):
    flag = dfs(i, i, ans[i])
    if flag == 0:
        break
if flag == 0:
    print(-1)
else:
    for i in range(n):
        for j in range(i+1):
            print(l[i][j], end=" ")
        print()
