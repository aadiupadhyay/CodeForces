a=int(input())
b=int(input())

ast=str(a)
bst=str(b)

c=str(a+b)
zeroC=''.join(c.split('0'))
c=int(zeroC)


zeroA=''.join(ast.split('0'))
zeroB=''.join(bst.split('0'))

ZA=int(zeroA)
ZB=int(zeroB)

d=ZA+ZB

if c==d:
    print('YES')
else:
    print('NO')
