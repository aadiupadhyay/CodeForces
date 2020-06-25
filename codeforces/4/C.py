d={}
def solve():

    s=input()
   
    if s not in d:
        print("OK")
        d[s]=1
    else:
        print(s+str(d[s]))
        d[s]+=1
 
        


for _ in range(int(input())):

    solve()
