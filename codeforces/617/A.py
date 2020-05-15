n=int(input())
c=0
x=5
while n>0:
    if n>=x:
        while n>=x:
            n=n-x
            c=c+1
    else:
        x=x-1
print(c)