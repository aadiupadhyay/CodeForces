n=int(input())
s=input()
for i in range(2,n+1):
    if n%i==0:
        x=s[:i]
        y=s[i:]
        s=x[::-1]+y
print(s)
