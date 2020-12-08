from math import gcd
n=int(input())
a=2
for i in range(2,n+1):
    a=a*i//gcd(a,i)
print(a+1)