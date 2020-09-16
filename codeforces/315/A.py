n=int(input())
 
A=[]
B=[]
for i in range(n):
  a,b=map(int,input().strip().split(' '))
  A.append(a)
  B.append(b)
count=0
 
for i in range(n):
  if A[i] not in B[:i] and A[i] not in B[i+1:]:
    count=count+1
    
    
print(count)