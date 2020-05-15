n=int(input())
s=input()
i=0
c=0
while i<n:
    x=s[i]
    j=i+1
  
    while j<n and s[j]==x:
        j=j+1
        c=c+1
    i=j
print(c)