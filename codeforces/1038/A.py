n,k=map(int,input().split())
st=input()
print(k*min(st.count(chr(65+i)) for i in range(k)))