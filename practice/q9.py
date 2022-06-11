x,y = map(int,input().split())
flag = 0

for i in range(0,x+1):
    if flag == 1:
        break
    for j in range(0,x-i+1):
        k = (y-10000*i-5000*j) // 1000
        if k >= 0 and i + j + k == x:
            flag = 1
            print(i,j,k)
            break

if flag==0:
    print("-1 -1 -1")