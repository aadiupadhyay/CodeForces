d={}

for  _ in range(int(input())):

    s=input()

    d[s]=d.get(s,0)+1
mini=-1000
for i,j in d.items():

    if j>mini:
        mini=j
        winner=i
print(winner)
