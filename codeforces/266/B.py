n,t=map(int,input().split())
s=input()
ss=[]
for i in s:
    ss.append(i)
for k in range(t):
    i=0
    j=1
    while i<=n-2 and j<=n-1:
        if ss[i]=="B" and ss[j]=="G":
            ss[j],ss[i]=ss[i],ss[j]
            i=j+1
            j=i+1
        else:
            i=i+1
            j=j+1
print("".join(ss))