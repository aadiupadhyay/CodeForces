for _ in range(int(input())):
    a,b=map(int,input().split())
    if a==b:
        print("0")
    elif ((a>b and (a-b)%2==0) or (b>a and (b-a)%2!=0)):
        print("1")
    else:
        print("2")