for _ in range(int(input())):
    s=input()
    x=len(s)
    if x<11:
        print(s)
    else:
        print(s[0]+str(x-2)+s[-1])