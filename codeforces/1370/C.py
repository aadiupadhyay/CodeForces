for _ in range(int(input())):
    n = int(input())
    ar = []
    i = 2
    hi = n
    while i * i <= hi:
        if n % i == 0:
            ar.append(i)
            n //= i
        else:
            i += 1
    if n > 1:
        ar.append(n)
    kek = 1
    for elem in ar:
        if elem % 2 == 1:
            kek = 0
    if hi == 1:
        print('FastestFinger')
    elif hi == 2:
        print('Ashishgup')
    elif kek:
        print('FastestFinger')
    elif len(ar) == 2 and (ar[0] + ar[1]) % 2 == 1:
        if ar[0] == 2 or ar[1] == 2:
            print('FastestFinger')
        else:
            print('Ashishgup')
    else:
        print('Ashishgup')