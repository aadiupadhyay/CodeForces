n,a,b=map(int,input().split())
z=(n+b)%n
ans=(a+z)%n
print(n if ans==0 else ans)