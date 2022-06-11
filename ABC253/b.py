h,w = map(int,input().split())

s = []

for i in range(h):
    s.append(input())

x = []
y = []
flag=0
for i in range(h):
    for j in range(w):
        if s[i][j] == "o" and flag == 0:
            x.append([i,j])
            flag = 1
        elif s[i][j] == "o" and flag == 1:
            y.append([i,j])
print(abs(x[0][0]-y[0][0]) + abs(x[0][1]-y[0][1]))