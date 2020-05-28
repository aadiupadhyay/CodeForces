import math
for _ in range(int(input())):
    n,m,x,y=map(int,input().split())
    l=[]
    b=0
    w=0
    for i in range(n):
        s=input()
        w+=s.count(".")
        l.append(s)

    if 2*x<=y:
        print(x*w)

    else:
        a=0
        for i in range(n):
            ss=""
            for j in range(m):

                if l[i][j]==".":
                    if l[i][j]==ss:

                        ss=""
                        a+=1
                        continue
                ss=l[i][j]

        print(a*y+(w-2*a)*x)
