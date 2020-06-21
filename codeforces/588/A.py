min_till=1000
c=0
for _ in range(int(input())):

    a,b=map(int,input().split())

    if b<min_till:
        min_till=b

    c+=(a*min_till)
print(c)
    
