for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    if sorted(a) == a:
        print("Yes")
    elif len(set(b)) == 1:
        print("No")
    else:
        print("Yes")