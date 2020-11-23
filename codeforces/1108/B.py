from collections import Counter
n=int(input())
l=list(map(int,input().split()))
a=max(l)
i=1
d=Counter(l)
while i*i <=a:
  if a%i==0:
    d[i]-=1
    if i!= a//i:
      d[a//i]-=1
  i+=1
l=[i for i in d if d[i]]
b=max(l)
print(a,b)
  