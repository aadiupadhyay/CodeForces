a="QRBPKN"
d={'Q':9,'R':5,'B':3,'N':3,'P':1,'K':0}
s,k=0,0
for i in range(8):
    p=input()
    for i in p:
        if i in a:
            s+=d[i]
        elif i in a.lower():
            k+=d[i.upper()]

if s>k:
    print("White")
elif s<k:
    print("Black")
else:
    print("Draw")
