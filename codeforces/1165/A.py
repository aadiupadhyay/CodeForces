n,x,y=map(int,input().split())
s=input()
s=s[::-1]
a=s[:x+1]
b=a[:y]
c=a[y+1:]
p=b.count("1")+c.count("1")
if a[y]!="1":
    p+=1
if a[-1]=="1":
    p-=1
print(p)
