I=input
for i in ','*int(I()):
    n = int(I())
    f= sum([int(j)%2 for j in I().split()])
    m=int(I())
    z=sum([int(j)%2 for j in I().split()])
    print((f*z)+(n-f)*(m-z))