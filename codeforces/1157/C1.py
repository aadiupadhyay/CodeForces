n = int(input())
l = list(map(int,input().split()))
 
ans = []
j = 0
k = n-1
 
seq = [0]
 
if n == 1:
    print(1)
    print('L')
 
else:
    while n:
        if l[j] > seq[-1] and l[k] > seq[-1]:
 
            if l[j] > l[k]:
                ans.append('R')
                seq.append(l[k])
                k-=1
                n-=1
            else:
                ans.append('L')
                seq.append(l[j])
                j+=1
                n-=1
 
        elif l[j] > seq[-1]:
            ans.append('L')
            seq.append(l[j])
            j+=1
            n-=1
        elif l[k] > seq[-1]:
            ans.append('R')
            seq.append(l[k])
            k-=1
            n-=1
        else:
            break
 
        #print(l[j:k+1])
    print(len(ans))
    print(*ans,sep='')