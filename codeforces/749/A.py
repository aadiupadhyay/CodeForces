n=int(input())
if n&1:
    n=n-3
    a=n//2
    print(a+1)
    print("2 "*a+"3")
else:
    a=n//2
    print(a)
    print("2 "*a)
