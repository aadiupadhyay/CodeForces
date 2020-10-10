from sys  import stdin,stdout

st=lambda:list(stdin.readline().strip())
li=lambda:list(map(int,stdin.readline().split()))
mp=lambda:map(int,stdin.readline().split())
inp=lambda:int(stdin.readline())
pr=lambda n: stdout.write(str(n)+"\n")

mod=1000000007

def solve():
    s=input().split('<')
    s=''.join(s)
    s=s.split('>')
    s.pop()
    h=[(s[0],0)]
    for i in s:
        if len(i)==2:
            if i[1]==h[-1][0]:
                #print(' '*2*h[-1][1]+'<'+h[-1][0]+'>')
                print(' '*2*(h[-1][1]-1)+'<'+i+'>')
                h.pop()
            else:
                h.append((i,h[-1][1]+1))
        else:
            h.append((i,h[-1][1]+1))
            print(' '*2*(h[-1][1]-1)+'<'+h[-1][0]+'>')

        #print(h)
            
    
    
for _ in range(1):
    solve()
