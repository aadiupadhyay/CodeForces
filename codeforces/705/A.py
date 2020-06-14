n=int(input())
s="I hate it"
p="I love it"
x=""
a="I hate that "
b="I love that "
for i in range(n-1):
    if i%2==0:
        x+=a
    else:
        x+=b
if n%2:
    x+=s
else:
    x+=p
print(x)
    
