N=int(input())
S=list(map(int,input().split()))
s=list(set(S))
s.sort()
x=len(s)
Z=0
for i in range(x-1):
  a=s[i]
  A=S.count(a)
  for j in range(x-i-1):
    b=s[i+1+j]
    B=S.count(b)
    t=[i for i in S if i>b and i<a+b]
    T=len(t)
    Z+=A*B*T
print(Z)