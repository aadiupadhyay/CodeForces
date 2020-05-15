k,n,w=map(int,input().split())
if ((k*((w+1)*w)//2)-n)>0:
    print((k*((w+1)*w)//2)-n)
else:
    print("0")