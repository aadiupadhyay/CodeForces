def fac(c):
    t = 1
    for i in range(1,c+1):
        t*=i
    return t
n = int(input())
f = fac(n)//fac(n//2)
d = fac(n//2)
print(f//(n//2)*(d//(n//2))//2)