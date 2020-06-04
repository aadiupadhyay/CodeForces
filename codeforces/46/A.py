n=int(input())
c=1
for i in range(1,n):
    z=(c+i)%n
    if z==0:
        z=n
    print(z,end=" ")
    c=z