n=int(input())
s=n+1
while True:
    if len(set(str(s)))==len(str(s)):
        print(s)
        break
    s+=1