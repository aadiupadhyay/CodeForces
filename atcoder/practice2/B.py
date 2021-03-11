def presum(indx,fen,n):
  s=0
  while indx>0:
    s=s+fen[indx]
    indx=indx-(indx&(-indx))
  return s
def query(l,r,fen,n):
  return presum(r,fen,n)-presum(l,fen,n)
def update(indx,delta,fen,n):
  while indx<n:
    fen[indx]+=delta
    indx=indx+(indx&(-indx))
  return fen
def buildtree(l,n):
  fen=[0]*n 
  for i in range(1,n):
    fen=update(i,l[i],fen,n)
  return fen
n,q=map(int,input().split())
l=list(map(int,input().split()))
l=[0]+l
n=n+1
fen=buildtree(l,n)
for i in range(q):
  a=list(map(int,input().split()))
  if a[0]==0:
    update(a[1]+1,a[2],fen,n)
  else:
    print(query(a[1],a[2],fen,n))
    		