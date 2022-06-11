n,a,b = list(map(int,input().split()))
n = str(n)
sum = 0
for i in range(0,int(n)+1):
    sum_num = i % 10 + (int(i/10) % 10) + (int(i/100) % 10) + (int(i/1000) % 10) + (int(i/10000) % 10)
    if a <= sum_num and b >= sum_num:
        sum += i
print(sum)