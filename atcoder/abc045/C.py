def rek(erg, rest):
    if not rest:
        return erg
 
    p = []
 
    for i in erg:
        p.append(i+"+"+rest[0])
        p.append(i+rest[0])
 
    return rek(p, rest[1:])
 
 
a = input()
 
erg = 0
comb = rek([a[0]], a[1:])
 
for i in comb:
    erg += eval(i)
 
print(erg)