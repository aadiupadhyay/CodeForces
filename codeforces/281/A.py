s=input()
if ord(s[0])>=97:
    print(chr(ord(s[0])-32)+s[1:])
else:
    print(s)