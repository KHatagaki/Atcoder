num_500 = input()
num_100 = input()
num_50 = input()
X = input()
cnt = 0

for i in range(0,int(num_500)+1):
    for j in range(0,int(num_100)+1):
        for k in range(0,int(num_50)+1):
            if 500*i + 100*j + 50*k == int(X):
                cnt += 1
print(cnt)