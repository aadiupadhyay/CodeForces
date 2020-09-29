n=int(input())
for i in range(n):
    a,b,c=map(int,input().split())
    print(min(min(a+b,a+c,b+c),(a+b+c)//2))