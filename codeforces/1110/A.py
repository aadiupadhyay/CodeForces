b, k = list(map(int, input().split()))
A = list(map(int, input().split()))
if b % 2 == 0 and A[-1] % 2 == 0:
    print('even')
elif b % 2 == 0 and A[-1] % 2 == 1:
    print('odd')
else:
    answer = 0
    frr = 0
    for i in range(k):
        answer += A[i]
        answer %= 2
    if answer % 2 == 0:
        print('even')
    else:
        print('odd')