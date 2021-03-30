# aadiupadhyay mobile se code krte
n,k = map(int, input ().split())
l = list(map(int,input(). split()))
ans = 0
c =sum(l[:k])
mi = c
for i in range(k,n):
  s=c-l[i-k] 
  s+=l[i]
  if s<mi:
    ans=i-k+1
    mi=s
  c=s
print(ans+1)