n=int(input())
a,b=n//7,n%7
x=2*a
print(x+(b==6),x+min(2,b))
