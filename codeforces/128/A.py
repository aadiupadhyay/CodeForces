d = [-1, 0, 1]
s = [raw_input() for _ in range(8)]
m = [(7, 0)]
for step in range(8):
    t = []
    for x, y in m:
        for dx in d:
            for dy in d:
                tx, ty = x + dx, y + dy
                if (tx, ty) not in t:
                    if 0 <= tx < 8 and 0 <= ty < 8:
                        ok = 1
                        if tx - step >= 0: ok &= s[tx - step][ty]!='S'
                        if tx - step - 1 >= 0: ok &= s[tx - step - 1][ty]!='S'
                        if ok: t.append((tx, ty))
    m = t
print m and 'WIN' or 'LOSE'