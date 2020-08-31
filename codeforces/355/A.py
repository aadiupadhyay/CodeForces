n,k=map(int,input().split())
if k==0:
    if n==1:
        print(0)
    else:
        print('No solution')
else:
    print(str(k)+'0'*(n-1))
  
    
