s=input()
l=[]
for i in s:
    if i!="+":
        l.append(int(i))
l.sort()
j=0
x=""
for i in s:
    if i!="+":
        x=x+str(l[j])
        j=j+1
    else:
        x=x+"+"
print(x)