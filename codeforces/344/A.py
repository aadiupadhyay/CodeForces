n=int(input())
c=1
s=input()
for i in range(n-1):
    x=input()
    if x[0]==s[-1]:
        c+=1
    s=x
print(c)
