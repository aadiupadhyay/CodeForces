min=-10000
p=0
for _  in range(int(input())):
    a,b=map(int,input().split())
    p=p-a+b
    if p>min:
        min=p
print(min)
