
def fact(n):
    i=2
    for i in range(2,int(n**0.5)+1):
        if n%i==0 and i not in l:
            return i
    return 0
for _ in range(int(input())):
    l=[]
    n=int(input())
    a=fact(n)
    l.append(a)
    if a!=0:
        b=fact(n/a)
    else:
        print("NO")
        continue
    if b!=0:
        z=(n//(a*b))
    else:
        print("NO")
        continue
    if z!=a and z!=b and z!=1:
        print("YES")
        print(a,b,z)
    else:
        print("NO")
    
