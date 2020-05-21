l=["H","Q","9"]
s=input()
c=0
for i in l:
    if i in s:
        c=1
        print("YES")
        break
if c==0:
    print("NO")