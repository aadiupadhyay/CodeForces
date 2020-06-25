n,m=map(int,input().split())
c=1
for i in range(n):
    if i%2==0:
        print("#"*m)
    else:
        if c%2:
            print("."*(m-1)+"#")
        else:
            print("#"+(m-1)*".")
        c+=1
    
        
