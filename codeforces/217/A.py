def solve(x_to_point, y_to_point, visited, x, y, points):
    for yi in x_to_point[x]:
        if (x, yi) not in visited:
            visited.add((x, yi))
            if (x, yi) in points:
                points.remove((x, yi))
            solve(x_to_point, y_to_point, visited, x, yi, points)
 
    for xi in y_to_point[y]:
        if (xi, y) not in visited:
            visited.add((xi, y))
            if (xi, y) in points:
                points.remove((xi, y))
            solve(x_to_point, y_to_point, visited, xi, y, points)
 
 
n = int(input())
x_to_point = {}
y_to_point = {}
points = set()
for i in range(n):
    x, y = list(map(int, input().split()))
    if x not in x_to_point.keys():
        x_to_point[x] = [y]
    else:
        x_to_point[x].append(y)
 
    if y not in y_to_point.keys():
        y_to_point[y] = [x]
    else:
        y_to_point[y].append(x)
 
    points.add((x, y))
 
ans = -1
while len(points) > 0:
    ans += 1
    visited = set()
    point = points.pop()
    visited.add(point)
    solve(x_to_point, y_to_point, visited, point[0], point[1], points)
 
print(ans)
 