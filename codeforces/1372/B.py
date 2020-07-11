import math

for i in range(int(input())):

    n=int(input())
    if n%2==0:
        print(n//2,n//2)
    else:
        l=[]
        i=1
        while i<=math.sqrt(n):
            if n%i==0:
                if n//i == i:
                    l.append(i)
                else:
                    l.append(n//i)
                    l.append(i)
            i+=1
        l.sort()
        print(l[-2],n-l[-2])