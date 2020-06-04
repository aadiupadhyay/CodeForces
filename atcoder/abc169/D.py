
def primefact(n):
    l=[]
    if n%2==0:
        while n%2==0:
            n=n//2
        l.append(2)
    for i in range(3,int(n**0.5)+1,2):
        if n%i==0:
            while n%i==0:
                n=n//i
            l.append(i)
    if n>2:
        l.append(n)
    return l

n=int(input())
c=0
a=(primefact(n))
for i in a:
    x=i
    while n%x==0:
        n=n//x
        c+=1
        x=x*i
print(c)
        
