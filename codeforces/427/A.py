n=int(input())
l=list(map(int,input().split()))
crime=0
police=0
for i in l:
    if i>0:
        police+=i
    elif i<0 and police>0:
        police-=1
    elif i<0 and police==0:
        crime+=1
print(crime)
