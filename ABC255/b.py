n,k = map(int,input().split())

a = list(map(int,input().split()))

x = []
y = []

idx = [1000000000000000000 for _ in range(n)]

for i in range(n):
    x_v,y_v = map(int,input().split())
    x.append(x_v)
    y.append(y_v)

for i in range(k):
    for j in range(n):
        if(idx[j] > ((x[j] - x[a[i]-1])**2 +  (y[j] - y[a[i]-1])**2) ** 0.5):
            idx[j] = ((x[j] - x[a[i]-1])**2 +  (y[j] - y[a[i]-1])**2) ** 0.5

print(max(idx))