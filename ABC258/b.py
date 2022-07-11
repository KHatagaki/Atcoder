n = int(input())

a = []

for i in range(n):
    b = input()
    b = list(b)
    a.append(b)
idx_max = ['0' for _ in range(n)]

max = 0
for i in range(n):
    for j in range(n):
        idx = []
        for k in range(n):
            idx.append(a[i][(j + k)%4])
        idx_max_s =  int("".join(map(str, idx_max)))
        idx_max_w =  int("".join(map(str, idx)))
        if(idx_max_s < idx_max_w):
            idx_max = idx

        idx = []
        for k in range(n):
            idx.append(a[(j + k)%4][i])
        idx_max_s =  int("".join(map(str, idx_max)))
        idx_max_w =  int("".join(map(str, idx)))
        if(idx_max_s < idx_max_w):
            idx_max = idx

        idx = []
        for k in range(n):
            idx.append(a[(i + k)%4][(j + k)%4])
        idx_max_s =  int("".join(map(str, idx_max)))
        idx_max_w =  int("".join(map(str, idx)))
        if(idx_max_s < idx_max_w):
            idx_max = idx

        idx = []
        for k in range(n):
            idx.append(a[(i + k)%4][(j - k + n)%4])
        idx_max_s =  int("".join(map(str, idx_max)))
        idx_max_w =  int("".join(map(str, idx)))
        if(idx_max_s < idx_max_w):
            idx_max = idx



for i in range(n):
    idx = []
    for j in range(n):
        x = (n-j+i)%4
        idx.append(a[j][x])
    idx_max_s =  int("".join(map(str, idx_max)))
    idx_max_w =  int("".join(map(str, idx)))
    if(idx_max_s < idx_max_w):
        idx_max = idx

print("".join(idx_max))
