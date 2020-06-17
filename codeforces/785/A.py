def solve():
    n=int(input())
    c=0
    d={"Tetrahedron":4,"Cube":6,"Octahedron":8,"Dodecahedron":12,"Icosahedron":20}
    for _ in range(n):
        s=input()
        c+=d[s]
    print(c)
solve()
