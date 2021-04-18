a, b = map(int, input().split())
if a == b:
    for i in range(1, a+1):
        print(i, -i, end=' ')
elif a > b:
    for i in range(1, a+1):
        print(i, end=' ')

    s = a*(a+1) // 2
    size = b
    ans = []
    for i in range(s, 0, -1):
        if i > s:
            continue
        if size*(size-1) // 2 <= (s-i):
            ans.append(-i)
            s -= i
            size -= 1
    print(*ans)


else:
    for i in range(1, b+1):
        print(-i, end=' ')

    s = b*(b+1)//2
    size = a
    ans = []
    for i in range(s, 0, -1):
        if i > s:
            continue
        if size*(size-1) // 2 <= (s-i):
            ans.append(i)
            s -= i
            size -= 1
    print(*ans)
