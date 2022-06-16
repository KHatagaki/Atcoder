r,c = map(int,input().split())

a = [[0 for _ in range(2)]for __ in range(2)]

a[0][0],a[0][1] = map(int,input().split())
a[1][0],a[1][1] = map(int,input().split())

print(a[r-1][c-1])

