def Sides():
    inputs = raw_input().split()
    a = int(inputs[0])
    b = int(inputs[1])
    c = int(inputs[2])
 
    x = (a*c/b)**0.5
    y = (b*c/a)**0.5
    z = (a*b/c)**0.5
 
    print int(4*(x+y+z))
 
Sides()