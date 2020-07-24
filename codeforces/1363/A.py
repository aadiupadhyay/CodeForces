t=int(input())
for i in range(t):
    n,x=input().split()
    n=int(n)
    x=int(x)
    b=list(map(int,input().split()))
    p=0
    q=0
    for j in range(n):
        if b[j]%2==0:
            p+=1
        else:
            q+=1
    if q==0:
        print("No")
    elif p==0:
        if x%2==0:
            print("No")
        else:
            print("Yes")
    elif x<q:
        print("Yes")
    else:
        if q%2==0:
            q=q-1
        if x<=(q+p):
            print("Yes")
        else:
            print("No")