n,m=map(int,input().split())
d={}
for i in range(n):
    p,q=input().split()
    d[q]=d.get(q,"")+p
for i in range(m):
    p,q=input().split()
    s=q[:-1]
    print(p,q,"#"+d[s])