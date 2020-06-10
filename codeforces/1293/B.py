n=int(input())
i=1;
sum=0.00000000;
while i<=n:
        sum+=i/n;
        n-=i;
print(sum)