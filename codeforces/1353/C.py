for _ in range(int(input())):
    n=int(input())
    if n==1:
        print("0")
    else:
        z=n//2
        s=0
        for i in range(1,z+1):
            s=s+(i)*(8*i)
        print(s)
            
