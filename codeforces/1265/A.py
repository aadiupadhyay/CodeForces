T = int(input())
for tc in range(T):
    s = [c for c in input()]
    n = len(s)
    i = 0
    while (i < n):
        if (s[i] == '?'):
            prv = 'd' if i == 0 else s[i - 1]
            nxt = 'e' if i + 1 >= n else s[i + 1]
            for x in ['a', 'b', 'c']:
                if (x != prv) and (x != nxt):
                    s[i] = x
                    break
        else:
            i += 1
           
    ok = True 
    for i in range(n - 1):
        if (s[i] == s[i + 1]):
            print("-1")
            ok = False
            break
    if (ok == True):  
        print("".join(s))