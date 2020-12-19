

for _ in range(int(input())):
    n = int(input())
    l = input()
    k = input()
    a, b = 0, 0
    for i in range(n):
        if l[i] > k[i]:
            a += 1
        elif l[i] < k[i]:
            b += 1

    if a > b:
        print('RED')
    elif a < b:
        print('BLUE')
    else:
        print('EQUAL')
