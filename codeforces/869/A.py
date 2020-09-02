n=int(input())
l=list(map(int,input().split()))
k=list(map(int,input().split()))
c=0
s=set((l+k))
for i in l:
    for j in k:
        a=i^j
        if a in s:
            c+=1
print('Karen' if c%2==0 else 'Koyomi')
