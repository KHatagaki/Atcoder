n = int(input())

a = list(map(int,input().split()))

dp = [[0 for _ in range(len(a))]for __ in range(3)]

for i in range(len(a)):
    dp[0][i] += 1

for i in range(1,3):
    for j in range(max(a)):
        if(dp[i-1][j])
        dp[i][j]