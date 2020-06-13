l=[]
for i in range(int(input())):
    s=input()
    l.append(s)
c=0
for i in range(len(l)):
    if l[i][0]==l[i][1]=="O":
        c=1
        l[i]="++"+l[i][2:]

        break
    elif l[i][3]==l[i][4]=="O":
        c=1
        l[i]=l[i][:3]+"++"

        break
if c==0:
    print("NO")
else:
    print("YES")
    for i in l:
        print(i)
    
        
    
