n=int(input())
s=list(input())
r=s.count("R")
g=s.count("G")
b=s.count("B")
if (r == 0 and g == 0):
    print("B")
elif r==1 and g==1 and b==0:
	print('B')
elif (r == 0 and b == 0):
	print('G')
elif r==1 and g==0 and b==1:
    print("G")
elif (b == 0 and g == 0):
    print("R")
elif r==0 and b==1 and g==1:
	print('R')
elif (r,g,b) == (1,g,0) or (r,g,b) == (0,g,1):
	print('BR')
elif (r,g,b) == (r,1,0) or (r,g,b) == (r,0,1):
	print('BG')
elif (r,g,b) == (1,0,b) or (r,g,b) == (0,1,b):
	print('GR')
else:
	print('BGR')