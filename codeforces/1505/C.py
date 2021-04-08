s = input()
x = [ord(i)-65 for i in s]
n = len(s)
if n <= 2:
    print('YES')
else:
    f = 0
    for i in range(2, n):
        if x[i] != (x[i-1]+x[i-2]) % 26:
            f = 1
            break
    if f:
        print('NO')
    else:
        print('YES')
