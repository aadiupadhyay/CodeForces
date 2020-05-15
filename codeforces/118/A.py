s=input().lower()
x=""
l=["a","e","o","i","u","y"]
for i in s:
    if i in l:
        continue
    else:
        x=x+"."+i
print(x)