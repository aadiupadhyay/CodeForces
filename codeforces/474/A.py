s=input()
t=input()
a="qwertyuiop"
b="asdfghjkl;"
c="zxcvbnm,./"

x=""
for i in t:
    if i in a:
        p=a.index(i)
        if s=="R":
            if p==0:
                x+=a[0]
            else:
                x+=a[p-1]
        else:
            if p==len(a)-1:
                x+=a[-1]
            else:
                x+=a[p+1]
    elif i in b:
        p=b.index(i)
        if s=="R":
            if p==0:
                x+=b[0]
            else:
                x+=b[p-1]
        else:
            if p==len(b)-1:
                x+=b[-1]
            else:
                x+=b[p+1]
    else:
        p=c.index(i)
        if s=="R":
            if p==0:
                x+=c[0]
            else:
                x+=c[p-1]
        else:
            if p==len(c)-1:
                x+=c[-1]
            else:
                x+=c[p+1]
print(x)
        
            

        
