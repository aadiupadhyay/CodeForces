import sys
input = sys.stdin.readline
#
Q = int(input())
for _ in range(Q):
    N = int(input())
    S = input().rstrip()
 
    P = "abacaba"
 
    ans = []
    for i in range(N-6):
        T = list(S)
        ok = True
        for j in range(7):
            if T[i+j] == "?":
                T[i+j] = P[j]
            elif S[i+j] != P[j]:
                ok = False
                break
        
        for j in range(N):
            if T[j] == "?":
                T[j] = "d"
 
        count = 0
        for j in range(N-6):
            if T[j:j+7] == list(P):
                count += 1  
 
        if ok and count == 1:
            ans = T
            break
    
    if not ans:
        print("No")
    else:
        print("Yes")
        print("".join(ans))