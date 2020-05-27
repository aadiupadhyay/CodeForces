n=int(input())
a=n%10
if a in [2,4,5,7,9]:
    print("hon")
elif a in [0,1,6,8]:
    print("pon")
else:
    print("bon")
