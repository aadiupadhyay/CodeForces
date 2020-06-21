for _ in range(int(input())):

    s=input()
    n=len(s)
    if s.count("0")==n:
        print(s)
    elif s.count("1")==n:
        print(s)
    else:
        x=""
        for i in range(n):
            x+="01"
        print(x)
