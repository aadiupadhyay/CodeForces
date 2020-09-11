s = str(input())
if s == 'a8' or s == 'a1' or s == 'h1' or s == 'h8':
    print(3)
elif s[0] == 'a' or s[0] == 'h' or s[1] == '1' or s[1] == '8':
    print(5)
else:
    print(8) 