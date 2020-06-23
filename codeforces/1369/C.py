def solve():

    n,k=map(int,input().split())

    l=list(map(int,input().split()))

    l.sort()

    x=list(map(int,input().split()))

    x.sort(reverse=True)

    c=l[::-1]

    l.sort()

    a=x.count(1)


    j,s=0,0
    
    for i in range(a):
        s+=2*c[i]

    for i in range(k):

        if x[i]!=1:

            s+=l[j]+c[a]
            a+=1
            j+=x[i]-1
        else:
            continue
    
    print(s)
            
            

    
        

    
    
    

for _ in range(int(input())):

    solve()
