l=[1,"January","February","March","April","May","June","July","August","September","October","November","December"]
s=input()
n=int(input())
x=l.index(s)
a=(x+n)%12
if a==0:
    a=12
print(l[a])
