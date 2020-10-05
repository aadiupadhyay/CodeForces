s=input()
a=s[::-1]
x=a.find('a')
if x!=-1:
  p=''
  x=len(s)-1-x
  ans=''
  for i in range(x+1):
    if s[i]!='a':
      p+=s[i]
    ans+=s[i]
  #print(p)
  #print(ans)
  f=0
  cur=''
  x+=1
  #print(x)
  while x<=len(s)-1:
    cur=s[x:]
    #print('cur',cur)
    if p==cur:
      print(ans)
      f=1
      break
    p+=s[x]
    ans+=s[x]
    x+=1
    #print(cur,p)
  #print(cur,p)
  
  
  if f==0:
    if p==cur:
      print(ans)
    else:
      print(':(')
else:
  n=len(s)
  if n&1:
    print(':(')
  else:
    a,b=s[:n//2],s[n//2:]
    if a==b:
      print(a)
    else:
      print(':(')