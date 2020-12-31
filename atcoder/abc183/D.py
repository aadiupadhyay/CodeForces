N,W=map(int,input().split())
S=[]
T=[]
P=[]

increase=[ 0 for _ in range( 2*10**5 +10)]
decrease=[ 0 for _ in range( 2*10**5 +10)]

for i in range(N):
    s,t,p=map(int,input().split())

    S.append(s)
    T.append(t)
    P.append(p)

    increase[s]+=p
    decrease[t]+=p

waterinuse=0
for i in range(2*10**5+10):
    waterinuse+=increase[i]
    waterinuse-=decrease[i]
    if waterinuse > W:
        print("No")
        exit()
print("Yes")



