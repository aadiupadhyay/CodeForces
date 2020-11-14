l,d,v,g,r=map(int,input().split())
s=(d/v)%(g+r)
ans=l/v
if s>=g:
	ans+=g+r-s
print(ans)
