import sympy as sp

a_list = list(map(int,input().split()))

h = []
w = []

for x in range(3):
    h.append(a_list[x])
    w.append(a_list[x+3])
print(h,w)


sp.var('a, b, c, d, e, f, g, j, i')
eq1=sp.Eq(h[0], a + b + c)
eq2=sp.Eq(h[1], d + e + f)
eq3=sp.Eq(h[2], g + j + i)
eq4=sp.Eq(w[0], a + d + g)
eq5=sp.Eq(w[1], b + e + j)
eq6=sp.Eq(w[2], c + f + i)
print(sp.solve ([eq1, eq2, eq3, eq4, eq5, eq6], [a,b,c,d,e,f,g,j,i]))
