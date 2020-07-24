for _ in range(int(input())):
    s=input()
    if s.count(s[0])==len(s):
        print(-1)
    else:
        if s==s[::-1]:
            print(s[1:]+s[0])
        else:
            print(s)
