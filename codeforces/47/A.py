n=int(input())
x=2*n
a=(-1+((1+4*x)**0.5))/2
b=(-1-((1+4*x)**0.5))/2
if (a>0 and a==int(a)) or (b>0 and b==int(b)):
    print("YES")
else:
    print("NO")
