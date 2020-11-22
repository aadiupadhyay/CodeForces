n=int(input())
print("AND 1 2")
aandb=int(input())
print("XOR 1 2")
axorb=int(input())
print("AND 1 3")
aandc=int(input())
print("XOR 1 3")
axorc=int(input())
print("AND 2 3")
bandc=int(input())
bxorc=axorb^axorc
num1=(2*(aandb)+axorb)
num2=(2*(bandc)+bxorc)
num3=(2*(aandc)+axorc)
z=(num1+num2+num3)//2
a=z-num2
b=z-num3
c=z-num1
arr=[0 for i in range(n)]
arr[0]=a
arr[1]=b
arr[2]=c
for i in range(n-3):
    print("XOR",end=" ")
    print(1,i+4)
    z=int(input())
    arr[i+3]=z^arr[0]
print("!",end=" ")
for i in arr:
    print(i,end=" ")
print()