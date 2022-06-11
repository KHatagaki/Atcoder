n,m,k = map(int,input().split())

dp_n = [[0] * k] * m


#for i in range(1,m):
i = 0
for i in n:
    for j in k:
        if i == 0:
            dp_n[i][-j] = 1